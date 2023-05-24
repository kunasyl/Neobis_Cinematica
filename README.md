Для создания билета в `showtimes/1/tickets/` (c JWT token):
```JSON
{
    "price_age": "Студенческий",
    "row": 5,
    "place": 5
}
```
или
```JSON
[
    {
        "price_age": "Студенческий",
        "row": 1,
        "place": 5
    },
    {
        "price_age": "Студенческий",
        "row": 1,
        "place": 6
    }
]
```

Для обновления нескольких билетов `showtimes/<int:pk>/tickets/update/` (c JWT token):
```JSON
[
    {
        "id": 1,
        "status": "Bought"
    },
    {
        "id": 2,
        "status": "Bought"
    }
]
```

Для создания билета `<int:pk>/tickets/reserve/`:
```JSON
{
    "showtime_id": 1,
    "seat_id": 198,
    "price_age": "Взрослый",
    "status": "Бронь"
}
```

Для создания фильма `movies/``:
```JSON
{
    "title": "Все страхи Бо",
    "genre": [
        "adventure"
    ],
    "age_rate": 16,
    "rating": 6.8,
    "is_active": true,
    "start_date": "10.05.2023",
    "end_date": "22.06.2023"
}
```
