from decouple import config

config = {
    'maxsize': config('QUEUE_MAXSIZE', 3, cast=int),
}
