from pydantic import BaseModel, Field, field_validator, ValidationError
from datetime import date, time
import re

# Модель для валидации данных
class AppointmentData(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="Имя клиента")
    car_type: str = Field(..., min_length=2, max_length=50, description="Тип автомобиля")
    service: str = Field(..., min_length=2, max_length=50, description="Услуга клиента")
    stylist: str = Field(..., min_length=2, max_length=50, description="Имя мастера")
    appointment_date: date = Field(..., description="Дата назначения")
    appointment_time: time = Field(..., description="Время назначения")
    user_id: int = Field(..., description="ID пользователя Telegram")
    phone_number: str = Field(..., description="Номер телефона в международном формате, начинающийся с '+'")

