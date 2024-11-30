from fastapi import FastAPI


def create_app() -> FastAPI:
    return FastAPI(
        title="Chat",
        docs_url="/api/docs",
        description="A simple fastapi chat",
        debug=True,
    )


if __name__ == "__main__":
    create_app()
