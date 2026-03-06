import os

# --- Strategy V2: Focused YES (ventanas por ciudad, hora Chile) ---
# Base: Score-Filtered YES (6-11.5¢, score ≥ 60, TP 15¢, sin stop loss)
# Cada ciudad tiene su propia ventana horaria (hora Chile UTC-3).
# Al cierre de cada ventana → cierre forzoso de sus posiciones.
#
# Ciudades y ventanas (hora Chile):
#   Ankara        04:00–06:00
#   Atlanta       11:00–15:00
#   Buenos Aires  11:00–17:00
#   London        08:00–10:00
#   Miami         11:00–17:00
#   NYC           11:00–17:00
#   Paris         06:00–10:00
#   Toronto       14:00–17:00
#   São Paulo     11:00–15:00
#   Seattle       16:00–20:00
#   Seoul         23:00–03:00  (cruza medianoche)
#   Wellington    18:00–20:00
#
# Por defecto: fines de semana HABILITADOS (mismas condiciones que semana)

# ── Day-of-week regime ────────────────────────────────────────────────────────
WEEKEND_ENABLED = os.environ.get("WEEKEND_ENABLED", "true").lower() == "true"

WEEKDAY_YES_MIN   = float(os.environ.get("WEEKDAY_YES_MIN",   0.06))
WEEKDAY_YES_MAX   = float(os.environ.get("WEEKDAY_YES_MAX",   0.115))
WEEKDAY_MIN_SCORE = int(os.environ.get("WEEKDAY_MIN_SCORE",   60))

WEEKEND_YES_MIN   = float(os.environ.get("WEEKEND_YES_MIN",   0.06))
WEEKEND_YES_MAX   = float(os.environ.get("WEEKEND_YES_MAX",   0.115))
WEEKEND_MIN_SCORE = int(os.environ.get("WEEKEND_MIN_SCORE",   60))

MIN_YES_PRICE   = WEEKDAY_YES_MIN
MAX_YES_PRICE   = WEEKDAY_YES_MAX
MIN_ENTRY_SCORE = WEEKDAY_MIN_SCORE

# ── Take profit ───────────────────────────────────────────────────────────────
TAKE_PROFIT_YES = float(os.environ.get("TAKE_PROFIT_YES", 0.15))

# ── Volume thresholds for scoring ─────────────────────────────────────────────
SCORE_VOLUME_HIGH = float(os.environ.get("SCORE_VOLUME_HIGH", 500))
SCORE_VOLUME_MID  = float(os.environ.get("SCORE_VOLUME_MID",  300))
SCORE_VOLUME_LOW  = float(os.environ.get("SCORE_VOLUME_LOW",  200))

# ── Price history ─────────────────────────────────────────────────────────────
PRICE_HISTORY_TTL = int(os.environ.get("PRICE_HISTORY_TTL", 3600))

# ── Position sizing (2.0%–3.0% inversamente proporcional al YES price) ────────
POSITION_SIZE_MIN = float(os.environ.get("POSITION_SIZE_MIN", 0.020))
POSITION_SIZE_MAX = float(os.environ.get("POSITION_SIZE_MAX", 0.030))

# ── Shared scan parameters ────────────────────────────────────────────────────
MIN_VOLUME        = float(os.environ.get("MIN_VOLUME", 200))
MONITOR_INTERVAL  = int(os.environ.get("MONITOR_INTERVAL", 30))
SCAN_DAYS_AHEAD   = int(os.environ.get("SCAN_DAYS_AHEAD", 1))
# ── Zona horaria del operador (Chile = UTC-3 en verano) ───────────────────────
# Todas las horas se evalúan en esta zona horaria
OBSERVER_UTC_OFFSET = int(os.environ.get("OBSERVER_UTC_OFFSET", -3))

# ── Ventanas horarias por ciudad (hora Chile) ─────────────────────────────────
# Formato: (open_h, open_m, close_h, close_m)
# A la hora de cierre se fuerza el cierre de todas las posiciones de esa ciudad.
CITY_WINDOWS = {
    "ankara":       ( 4,  0,  6,  0),
    "atlanta":      (11,  0, 15,  0),
    "buenos-aires": (11,  0, 17,  0),
    "london":       ( 8,  0, 10,  0),
    "miami":        (11,  0, 17,  0),
    "nyc":          (11,  0, 17,  0),
    "paris":        ( 6,  0, 10,  0),
    "toronto":      (14,  0, 17,  0),
    "sao-paulo":    (11,  0, 15,  0),
    "seattle":      (16,  0, 20,  0),
    "seoul":        (23,  0,  3,  0),  # cruza medianoche
    "wellington":   (18,  0, 20,  0),
}
MAX_POSITIONS     = int(os.environ.get("MAX_POSITIONS", 20))
PRICE_UPDATE_INTERVAL = int(os.environ.get("PRICE_UPDATE_INTERVAL", 10))

# ── Geographic correlation limits ─────────────────────────────────────────────
MAX_REGION_EXPOSURE = float(os.environ.get("MAX_REGION_EXPOSURE", 0.25))

REGION_MAP = {
    "chicago": "midwest",       "denver": "midwest",
    "dallas": "south",          "houston": "south",
    "atlanta": "south",         "miami": "south",         "phoenix": "south",
    "boston": "northeast",      "nyc": "northeast",
    "seattle": "pacific",       "los-angeles": "pacific",
    "london": "europe",         "paris": "europe",        "ankara": "europe",
    "wellington": "southern",   "buenos-aires": "southern", "sao-paulo": "southern",
    "seoul": "asia",
}

# ── Capital ───────────────────────────────────────────────────────────────────
INITIAL_CAPITAL = float(os.environ.get("INITIAL_CAPITAL", 100.0))
AUTO_MODE       = os.environ.get("AUTO_MODE", "true").lower() == "true"
AUTO_START      = os.environ.get("AUTO_START", "true").lower() == "true"

# ── API ───────────────────────────────────────────────────────────────────────
GAMMA = os.environ.get("GAMMA_API", "https://gamma-api.polymarket.com")

# ── City UTC offsets ───────────────────────────────────────────────────────────
CITY_UTC_OFFSET = {
    "chicago":      -6,
    "dallas":       -6,
    "atlanta":      -5,
    "miami":        -5,
    "nyc":          -5,
    "boston":       -5,
    "toronto":      -5,
    "seattle":      -8,
    "los-angeles":  -8,
    "houston":      -6,
    "phoenix":      -7,
    "denver":       -7,
    "london":        0,
    "paris":         1,
    "ankara":        3,
    "seoul":         9,
    "wellington":   13,
    "sao-paulo":    -3,
    "buenos-aires": -3,
}

# ── V2: Ciudades activas con ventana horaria propia ───────────────────────────
WEATHER_CITIES = [
    "ankara",
    "atlanta",
    "buenos-aires",
    "london",
    "miami",
    "nyc",
    "paris",
    "toronto",
    "sao-paulo",
    "seattle",
    "seoul",
    "wellington",
]
