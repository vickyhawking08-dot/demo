from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles


# =========================================================
# APP CONFIG
# =========================================================

BASE_DIR = Path(__file__).resolve().parent

TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"


app = FastAPI(
    title="Sowmiya & Anvith - Family Chat",
    description="Fun mother and daughter conversation website",
    version="1.0.0",
)


# =========================================================
# STATIC FILES
# =========================================================

app.mount(
    "/static",
    StaticFiles(directory=str(STATIC_DIR)),
    name="static",
)


# =========================================================
# CONVERSATION
# =========================================================

conversation = [
    {
        "speaker": "Sowmiya",
        "role": "mother",
        "message": "Anvithhhh... enna panra ma? 😏",
        "emoji": "👩",
    },
    {
        "speaker": "Anvith",
        "role": "daughter",
        "message": "Nothing maa... summa phone paathutu iruken 😌",
        "emoji": "👧",
    },
    {
        "speaker": "Sowmiya",
        "role": "mother",
        "message": "Phone paakradhu mattum dhaan unakku velaya? Morning la irundhu phone kai-la dhaan irukku! 😂",
        "emoji": "👩",
    },
    {
        "speaker": "Anvith",
        "role": "daughter",
        "message": "Maa, phone illaama naan epdi survive panradhu? Idhu en oxygen 😭📱",
        "emoji": "👧",
    },
    {
        "speaker": "Sowmiya",
        "role": "mother",
        "message": "Oxygen-aa? Appo sapadu venama? 😑",
        "emoji": "👩",
    },
    {
        "speaker": "Anvith",
        "role": "daughter",
        "message": "Sapadu venum maa... especially neenga panra saapadu 😋❤️",
        "emoji": "👧",
    },
    {
        "speaker": "Sowmiya",
        "role": "mother",
        "message": "Ahaaa... ippo dhaan puriyudhu. Enna venum? 😏",
        "emoji": "👩",
    },
    {
        "speaker": "Anvith",
        "role": "daughter",
        "message": "Onnum illa maa... 😇",
        "emoji": "👧",
    },
    {
        "speaker": "Sowmiya",
        "role": "mother",
        "message": "Indha 'onnum illa' dialogue sonna udane enakku bayama irukku! 😂",
        "emoji": "👩",
    },
    {
        "speaker": "Anvith",
        "role": "daughter",
        "message": "Actually... konjam cash venum maa 🥹",
        "emoji": "👧",
    },
    {
        "speaker": "Sowmiya",
        "role": "mother",
        "message": "Appadi sollu! Love, affection ellam cash varum varaikkum dhaana? 😂",
        "emoji": "👩",
    },
    {
        "speaker": "Anvith",
        "role": "daughter",
        "message": "Maa pleaseee... last time dhaan 😭",
        "emoji": "👧",
    },
    {
        "speaker": "Sowmiya",
        "role": "mother",
        "message": "Last time-aa? Nee sonna 'last time' count panna calculator kooda hang aagidum! 🤣",
        "emoji": "👩",
    },
    {
        "speaker": "Anvith",
        "role": "daughter",
        "message": "Okay okay maa... indha time genuine 😭🙏",
        "emoji": "👧",
    },
    {
        "speaker": "Sowmiya",
        "role": "mother",
        "message": "Seri seri. Evlo venum?",
        "emoji": "👩",
    },
    {
        "speaker": "Anvith",
        "role": "daughter",
        "message": "Just ₹500 maa... 😇",
        "emoji": "👧",
    },
    {
        "speaker": "Sowmiya",
        "role": "mother",
        "message": "₹500-aa?! Enna panna pora?",
        "emoji": "👩",
    },
    {
        "speaker": "Anvith",
        "role": "daughter",
        "message": "Friends kooda konjam outing maa 😌",
        "emoji": "👧",
    },
    {
        "speaker": "Sowmiya",
        "role": "mother",
        "message": "Outing-ku ₹500... return ticket-ku yaaru kuduppa? 😂",
        "emoji": "👩",
    },
    {
        "speaker": "Anvith",
        "role": "daughter",
        "message": "Maa, naan auto la pogala... friends drop pannuvanga 😌",
        "emoji": "👧",
    },
    {
        "speaker": "Sowmiya",
        "role": "mother",
        "message": "Hmm... sari. Aana night late aaga koodadhu.",
        "emoji": "👩",
    },
    {
        "speaker": "Anvith",
        "role": "daughter",
        "message": "Promise maa ❤️",
        "emoji": "👧",
    },
    {
        "speaker": "Sowmiya",
        "role": "mother",
        "message": "And phone charge panni vechuko.",
        "emoji": "👩",
    },
    {
        "speaker": "Anvith",
        "role": "daughter",
        "message": "Phone 100% charge maa 😎🔋",
        "emoji": "👧",
    },
    {
        "speaker": "Sowmiya",
        "role": "mother",
        "message": "Phone 100%. Nee 10% kooda responsible illa! 🤦‍♀️😂",
        "emoji": "👩",
    },
    {
        "speaker": "Anvith",
        "role": "daughter",
        "message": "Maaaaa 😭😂❤️",
        "emoji": "👧",
    },
    {
        "speaker": "Sowmiya",
        "role": "mother",
        "message": "Seri po ma. Enjoy pannitu safe-ah vaa ❤️",
        "emoji": "👩",
    },
    {
        "speaker": "Anvith",
        "role": "daughter",
        "message": "Love you maa! ❤️🥹",
        "emoji": "👧",
    },
    {
        "speaker": "Sowmiya",
        "role": "mother",
        "message": "Love you too... aana ₹500-ku receipt venum! 😂",
        "emoji": "👩",
    },
    {
        "speaker": "Anvith",
        "role": "daughter",
        "message": "Aiyo maa! 😂😂😂",
        "emoji": "👧",
    },
]


# =========================================================
# HOME PAGE
# =========================================================

@app.get("/")
async def home():
    index_file = TEMPLATES_DIR / "index.html"

    return FileResponse(
        path=str(index_file),
        media_type="text/html",
    )


# =========================================================
# CONVERSATION API
# =========================================================

@app.get("/api/conversation")
async def get_conversation():
    return JSONResponse(
        content={
            "success": True,
            "total": len(conversation),
            "conversation": conversation,
        }
    )


# =========================================================
# HEALTH CHECK
# =========================================================

@app.get("/api/health")
async def health():
    return {
        "status": "ok",
        "message": "Sowmiya & Anvith chat server is running",
    }

