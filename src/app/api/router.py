import fastapi as fa
from app.api.endpoints.users import router as router_user
from app.api.endpoints.materials import router as router_material

router = fa.APIRouter(prefix='/api')
router.include_router(router_user)
router.include_router(router_material)
