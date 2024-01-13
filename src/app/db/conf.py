try:
    from core.settings import database_url
    import user.models

    models = ['aerich.models', 'user.models']

except ImportError:
    from app.core.settings import database_url

    models = ['aerich.models', 'app.user.models', 'app.material.models']

TORTOISE_ORM = {
    "connections": {"default": database_url},
    "apps": {
        "models": {
            "models": models,
            "default_connection": "default",
        },
    },
}
