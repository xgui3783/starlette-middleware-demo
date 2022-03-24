from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def homepage(request):
    return JSONResponse({'hello': 'world'})

routes = [
    Route("/", endpoint=homepage)
]

app = Starlette(debug=True, routes=routes)

@app.middleware('http')
async def m0(request, call_next):
    print("m0 pre")
    response = await call_next(request)
    print("m0 post")
    return response

@app.middleware('http')
async def m1(request, call_next):
    print("m1 pre")
    response = await call_next(request)
    print("m1 post")
    return response
