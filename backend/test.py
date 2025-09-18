# test.py
import socketio
import sys
from service import predict_all

sys.stdout.reconfigure(
    encoding="utf-8", line_buffering=True, write_through=True)

sio = socketio.AsyncServer(
    async_mode="asgi",
    cors_allowed_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    logger=False,
    engineio_logger=False,
)
app = socketio.ASGIApp(sio)


@sio.event
async def connect(sid, environ):
    print("connected:", sid)


@sio.event
async def process_form(sid, data: dict):
    # Input vector init
    X = []
    # For every value sent by the user append the value into our
    # input vector
    for _, v in data.items():
        X.append(v)

    # Do KNN, Logistic regression and Naive bayes to get
    # the probability of winning or loosing

    # res is going to be our results from our tests
    # based on KNN, Logistic regression and Naive bayes

    res = predict_all(X)

    return flatten_scores(res)


def flatten_scores(scores: dict, round_to=None) -> dict:
    out = {"ok": True}
    for model, probs in scores.items():
        if not isinstance(probs, dict):
            out[model] = probs
            continue
        for k, v in probs.items():
            key = f"{model}{k.replace('_','')}"   # p_1 -> p1
            if isinstance(v, (int, float)) and round_to is not None:
                v = round(v, round_to)
            out[key] = v
    return out
