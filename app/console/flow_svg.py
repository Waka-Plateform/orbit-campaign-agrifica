from fastapi import APIRouter, Response
router = APIRouter(prefix="/api/console", tags=["console"])
NODES=["A1 Email","A2 SMS","A3 WhatsApp","A4 QR/USSD","B Interaction?","C Web text","D Web voice","E Avatar","G Voice follow-up","H Accept?","I Data web","J Data call","END"]
@router.get("/flow.svg")
def flow_svg(mode: str = "runtime"):
    h=80+len(NODES)*70
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="980" height="{h}" viewBox="0 0 980 {h}"><style>text{{font-family:Arial;font-size:14px}} .n{{fill:#fff7ed;stroke:#E8832A;stroke-width:2}} .k{{font-size:11px;fill:#555}}</style>']
    y=40
    for i,n in enumerate(NODES):
        parts.append(f'<rect class="n" x="330" y="{y}" width="320" height="44" rx="10"/><text x="350" y="{y+26}">{n}</text>')
        if mode=="runtime": parts.append(f'<text class="k" x="560" y="{y+26}">sent 0 · conv 0</text>')
        if i < len(NODES)-1: parts.append(f'<path d="M490 {y+44} L490 {y+70}" stroke="#555" marker-end="url(#a)"/>')
        y += 70
    parts.insert(1,'<defs><marker id="a" markerWidth="10" markerHeight="10" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L6,3 z" fill="#555"/></marker></defs>')
    parts.append('</svg>')
    return Response("".join(parts), media_type="image/svg+xml")
