#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from pathlib import Path
# from SocialAnalytics.app.core.conf import settings

# Get the project root directory
# Or use an absolute path, pointing to the SocialAnalytics directory, such as windows：BasePath = D:\git_project\fastapi_mysql\SocialAnalytics
BasePath = Path(__file__).resolve().parent.parent.parent
print(BasePath)

# # Migration file storage path
# Versions = os.path.join(BasePath, 'app', 'alembic', 'versions')

# # Log file path
# LogPath = os.path.join(BasePath, 'app', 'log')

# # RBAC model.conf file path
# RBAC_MODEL_CONF = os.path.join(BasePath, 'app', 'core', settings.CASBIN_RBAC_MODEL_NAME)

# # Offline IP database path
# IP2REGION_XDB = os.path.join(BasePath, 'app', 'static', 'ip2region.xdb')
