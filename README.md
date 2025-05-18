[//]: # (ceate a project usign uv)
uv init project-name

flask db init
flask db migrate -m "initial"
flask db upgrade