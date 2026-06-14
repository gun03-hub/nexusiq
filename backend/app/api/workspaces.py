from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.db.database import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.models.workspace import Workspace
from app.schemas.workspace import (
    WorkspaceCreate,
    WorkspaceResponse
)

router = APIRouter(
    prefix="/workspaces",
    tags=["Workspaces"]
)


@router.get("/")
def get_workspaces():
    return {
        "message": "Workspace endpoint working"
    }

@router.post(
    "/",
    response_model=WorkspaceResponse
)
def create_workspace(
    workspace: WorkspaceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    new_workspace = Workspace(
        name=workspace.name,
        owner_id=current_user.id
    )

    db.add(new_workspace)
    db.commit()
    db.refresh(new_workspace)

    return new_workspace