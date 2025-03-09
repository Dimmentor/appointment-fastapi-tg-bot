from pydantic import BaseModel, Field, field_validator, ValidationError
from datetime import date, time
import re


# Модель для валидации данных
class AppointmentData(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="Имя клиента")
    car_type: str = Field(..., min_length=2, max_length=50, description="Тип автомобиля")
    service: str = Field(..., min_length=2, max_length=50, description="Услуга клиента")
    stylist: str = Field(..., min_length=2, max_length=50, description="Имя мастера")
    appointment_date: date = Field(..., description="Дата назначения")  # Переименовал поле
    appointment_time: time = Field(..., description="Время назначения")  # Переименовал поле
    user_id: int = Field(..., description="ID пользователя Telegram")
    phone_number: str = Field(..., description="Номер телефона в международном формате, начинающийся с '+'")

    # @field_validator("phone_number")
    # @classmethod
    # def validate_phone_number(cls, value: str) -> str:
    #     if not re.match(r'^\+\d{1,15}$', value):
    #         raise ValueError('Номер телефона должен начинаться с "+" и содержать от 1 до 15 цифр')
    #     return value
    #
    # @field_validator("appointment_date")
    # @classmethod
    # def validate_appointment_date(cls, value: date) -> date:
    #     if value < date.today():
    #         raise ValueError('Дата назначения не может быть меньше сегодняшней')
    #     return value
