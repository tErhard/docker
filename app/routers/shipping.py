from fastapi import APIRouter, HTTPException

router = APIRouter()

shipments = [
    {
        "id": 1,
        "sender": "John Doe",
        "recipient": "Jane Smith",
        "status": "in_transit"
    },
]

@router.post("/shipments/")
async def create_shipment(sender: str, recipient: str):
    new_shipment = {
        "id": len(shipments) + 1,
        "sender": sender,
        "recipient": recipient,
        "status": "created"
    }
    shipments.append(new_shipment)
    return new_shipment

@router.get("/shipments/{shipment_id}")
async def get_shipment(shipment_id: int):
    for shipment in shipments:
        if shipment["id"] == shipment_id:
            return shipment
    raise HTTPException(status_code=404, detail="Shipment not found")

@router.put("/shipments/{shipment_id}")
async def update_shipment_status(shipment_id: int, new_status: str):
    for shipment in shipments:
        if shipment["id"] == shipment_id:
            shipment["status"] = new_status
            return shipment
    raise HTTPException(status_code=404, detail="Shipment not found")
