from fastapi import FastAPI


def create_app():
    return FastAPI(
        title="Chat",
        docs_url="/api/docs",
        description="A simple fastapi chat"
    )