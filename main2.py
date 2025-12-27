import asyncio
import base64
import traceback
from pathlib import Path

import httpx

from pydantic_cpd.cdp.page.commands import (
    ScreencastFrameAckParams,
    StartScreencastParams,
)
from pydantic_cpd.cdp.page.library import PageClient
from pydantic_cpd.client import CDPClient


async def save_frame(frame_data: str, frame_number: int, output_dir: Path):
    """Save screencast frame as JPEG"""
    try:
        image_bytes = base64.b64decode(frame_data)
        output_path = output_dir / f"frame_{frame_number:04d}.jpg"
        output_path.write_bytes(image_bytes)
        print(f"Saved frame {frame_number}")
    except Exception as e:
        print(f"Error saving frame {frame_number}: {e}")
        traceback.print_exc()


async def get_ws_url() -> str:
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:9222/json")
        pages = response.json()

        if not pages:
            raise RuntimeError(
                "No pages found. Is Chrome running with --remote-debugging-port=9222?"
            )

        return pages[0]["webSocketDebuggerUrl"]


async def main():
    output_dir = Path("screencast_frames")
    output_dir.mkdir(exist_ok=True)

    frame_count = 0

    ws_url = await get_ws_url()
    print(f"Connecting to: {ws_url}")

    async with CDPClient(ws_url) as client:
        page = PageClient(client)

        # Register event handler for screencast frames
        @client.on("Page.screencastFrame")
        async def on_frame(params, cdp_session_id):  # ← Umbenennen für Klarheit
            nonlocal frame_count

            try:
                print(f"Received frame event: {params}")  # Debug

                frame_count += 1

                # params ist entweder ein dict oder Pydantic model
                if isinstance(params, dict):
                    frame_data = params["data"]
                    screencast_session_id = params["sessionId"]
                else:
                    frame_data = params.data
                    screencast_session_id = params.session_id

                # Save the frame
                await save_frame(frame_data, frame_count, output_dir)

                # Acknowledge frame - je nach deiner Implementierung:
                # Option 1: Direkt als Parameter
                await page.screencast_frame_ack(
                    params=ScreencastFrameAckParams(session_id=screencast_session_id)
                )

                # Option 2: Als Params-Objekt (falls dein Generator das so macht)
                # from pydantic_cpd.cdp.page.commands import ScreencastFrameAckParams
                # await page.screencast_frame_ack(
                #     ScreencastFrameAckParams(session_id=screencast_session_id)
                # )

            except Exception as e:
                print(f"Error in frame handler: {e}")
                traceback.print_exc()

        # Optional: Handle visibility changes
        @client.on("Page.screencastVisibilityChanged")
        async def on_visibility_changed(params, cdp_session_id):
            try:
                visible = (
                    params.get("visible")
                    if isinstance(params, dict)
                    else params.visible
                )
                print(f"Screencast visibility: {visible}")
            except Exception as e:
                print(f"Error in visibility handler: {e}")
                traceback.print_exc()

        # Enable page domain
        await page.enable()

        # Start screencast
        result = await page.start_screencast(
            StartScreencastParams(
                format="jpeg",
                quality=80,
                max_width=1280,
                max_height=720,
                every_nth_frame=1,
            )
        )
        print(f"Screencast started: {result}")

        print("Recording screencast... Press Ctrl+C to stop")

        try:
            # Keep running and receiving frames
            await asyncio.sleep(30)  # Record for 30 seconds
        except KeyboardInterrupt:
            print("\nStopping...")
        finally:
            # Stop screencast
            await page.stop_screencast()
            print(f"Recorded {frame_count} frames")


if __name__ == "__main__":
    asyncio.run(main())
