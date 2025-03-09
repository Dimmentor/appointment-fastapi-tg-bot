from aiogram.types import Message
from app.bot.keyboards.kbs import main_keyboard


def get_about_us_text() -> str:
    return """
🌟 Современная автомойка 'Зеркало'" 🌟

Добро пожаловать на нашу автомойку! Мы — команда профессионалов, которые любят автомобили и заботятся о каждом клиенте.

✨ Наша цель — предоставить вашему автомобилю безупречный уход и восстановить его первозданный вид.
С момента открытия мы зарекомендовали себя как надежное место для чистки и защиты автомобилей.

🎨 С момента открытия мы зарекомендовали себя как надежное место для чистки и защиты автомобилей. Мы используем только современные средства и оборудование, обеспечивая качественную мойку, полировку и защиту кузова. В нашем ассортименте услуг — как стандартные, так и специализированные процедуры, включая химчистку салона и восстановление фар.

🐒️‍🎨 Наши мастера:
Талантливая команда профессионалов с многолетним опытом и постоянным стремлением к совершенству. Мы следим за последними трендами и используем инновационные техники.

🌿 Наша атмосфера:
Мы понимаем, что каждый автомобиль уникален, поэтому подходим к каждому клиенту с индивидуальным вниманием. Наши опытные мастера всегда готовы предложить лучшие решения и советы по уходу за вашим автомобилем.

Поддержите внешний вид вашего автомобиля и доверьте его уход нашим специалистам. Мы гарантируем качество и внимание к деталям, чтобы каждый визит оставлял только положительные эмоции!

💎 Почему выбирают нас:
• Индивидуальный подход к каждому автомобилю
• Использование премиальной химии
• Гарантия качества и результата
• Уютная и стильная обстановка
• Удобное расположение в центре города


✨ Красота вашего автомобиля - наше призвание! ✨
"""


async def greet_user(message: Message, is_new_user: bool) -> None:
    """
    Приветствует пользователя и отправляет соответствующее сообщение.
    """
    greeting = "Добро пожаловать" if is_new_user else "С возвращением"
    status = "Вы успешно зарегистрированы!" if is_new_user else "Рады видеть вас снова!"
    await message.answer(
        f"{greeting}, <b>{message.from_user.full_name}</b>! {status}\n"
        "Чем я могу помочь вам сегодня?",
        reply_markup=main_keyboard(user_id=message.from_user.id, first_name=message.from_user.first_name)
    )
