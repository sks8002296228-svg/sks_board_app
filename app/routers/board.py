from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import logging

router = APIRouter()
logger = logging.getLogger("BOARD_WEBSOCKET")

active_connections: list[WebSocket] = []

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)
    logger.info(f"Client connected. Active: {len(active_connections)}")
    
    try:
        while True:
            data = await websocket.receive_text()
            for client in active_connections:
                if client != websocket:
                    await client.send_text(data)
    except WebSocketDisconnect:
        active_connections.remove(websocket)
        logger.info(f"Client disconnected. Remaining: {len(active_connections)}")
