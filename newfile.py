from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.graphics import Rectangle, Color
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
import random
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# تنظیمات اولیه پنجره
Window.clearcolor = get_color_from_hex('#FFFFFF')  # پس‌زمینه سفید

# Neural Network with TensorFlow
class TensorFlowNeuralNetwork:
    def __init__(self):
        self.history = []  # Stores user choices
        self.model = self.build_model()

    def build_model(self):
        model = Sequential([
            Dense(10, input_shape=(7,), activation='relu'),  # Hidden layer
            Dense(7, activation='softmax')  # Output layer
        ])
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def train(self, inputs, targets):
        inputs = np.array(inputs)
        targets = np.array(targets)
        self.model.fit(inputs, targets, epochs=10, verbose=0)

    def predict(self, inputs):
        inputs = np.array(inputs)
        prediction = self.model.predict(inputs, verbose=0)
        return np.argmax(prediction) + 1

    def update_history(self, choice):
        self.history.append(choice)

# Screens
class BaseScreen(Screen):
    def set_background(self, color):
        with self.canvas.before:
            Color(*color)
            self.bg = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self.update_bg, pos=self.update_bg)

    def update_bg(self, *args):
        if hasattr(self, 'bg'):
            self.bg.size = self.size
            self.bg.pos = self.pos

from kivy.graphics import Color, Rectangle

from kivy.uix.image import Image

from kivy.uix.image import Image

from kivy.uix.image import Image

from kivy.uix.image import Image
from kivy.clock import Clock

from kivy.uix.image import Image
from kivy.clock import Clock

from kivy.uix.image import Image
from kivy.clock import Clock

from kivy.uix.image import Image

class LoadingScreen(BaseScreen):
    def on_enter(self):
        self.clear_widgets()
        with self.canvas.before:
            Color(0.17, 0.24, 0.31, 1)  # معادل #2c3e50 در RGB
            self.bg = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self.update_bg, pos=self.update_bg)

        # نمایش GIF با اندازه‌گیری خودکار نسبت به صفحه
        self.loading_gif = Image(
            source='/storage/emulated/0/bin/loading.gif',  # مسیر فایل GIF
            size_hint=(1, 1),  # اندازه بر اساس سایز صفحه
            allow_stretch=True,  # اجازه تغییر اندازه برای تطابق با صفحه
            keep_ratio=True,  # حفظ نسبت ابعاد
            pos_hint={'center_x': 0.5, 'center_y': 0.5}  # مرکز صفحه
        )
        self.add_widget(self.loading_gif)

        # اجرای schedule_switch با کمی تأخیر
        Clock.schedule_once(self.schedule_switch, 5)

    def schedule_switch(self, dt):
        Clock.schedule_once(self.switch_to_main, 5)

    def switch_to_main(self, dt):
        self.manager.transition = FadeTransition(duration=0.5)
        self.manager.current = 'main_menu'









class MainMenuScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_background(get_color_from_hex('#3498db'))  # پس‌زمینه آبی
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20, size_hint=(0.8, 0.8), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # عنوان بازی
        title_label = Label(
            text="Neural Game",
            font_size='48sp',
            font_name='/storage/emulated/0/bin/Roboto-Bold.ttf',
            color=get_color_from_hex('#ecf0f1'),
            size_hint=(1, 0.4)
        )
        layout.add_widget(title_label)

        # دکمه‌ها
        start_button = Button(
            text="Start Game",
            size_hint=(1, 0.2),
            background_normal='',
            background_color=get_color_from_hex('#2ecc71'),  # سبز
            color=get_color_from_hex('#ecf0f1'),
            font_size='24sp',
            font_name='/storage/emulated/0/bin/Roboto-Medium.ttf',
            on_release=self.start_game
        )

        about_button = Button(
            text="About Us",
            size_hint=(1, 0.2),
            background_normal='',
            background_color=get_color_from_hex('#e67e22'),  # نارنجی
            color=get_color_from_hex('#ecf0f1'),
            font_size='24sp',
            font_name='/storage/emulated/0/bin/Roboto-Medium.ttf',
            on_release=self.show_about
        )

        settings_button = Button(
            text="Settings",
            size_hint=(1, 0.2),
            background_normal='',
            background_color=get_color_from_hex('#9b59b6'),  # بنفش
            color=get_color_from_hex('#ecf0f1'),
            font_size='24sp',
            font_name='/storage/emulated/0/bin/Roboto-Medium.ttf',
            on_release=self.show_settings
        )

        # انیمیشن برای دکمه‌ها
        self.animate_button(start_button)
        self.animate_button(about_button)
        self.animate_button(settings_button)

        layout.add_widget(start_button)
        layout.add_widget(about_button)
        layout.add_widget(settings_button)

        self.add_widget(layout)

    def animate_button(self, button):
        anim = Animation(opacity=0, duration=0) + Animation(opacity=1, duration=1)
        anim.start(button)

    def start_game(self, instance):
        game_screen = self.manager.get_screen('game_screen')
        game_screen.reset_game(None)
        game_screen.enable_all_buttons()
        self.manager.transition = FadeTransition(duration=0.5)
        self.manager.current = 'game_screen'

    def show_about(self, instance):
        self.manager.transition = FadeTransition(duration=0.5)
        self.manager.current = 'about_screen'

    def show_settings(self, instance):
        self.manager.transition = FadeTransition(duration=0.5)
        self.manager.current = 'settings_screen'

class AboutScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_background(get_color_from_hex('#34495e'))  # پس‌زمینه خاکستری تیره
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        about_label = Label(
            text="This is a simple AI-based game where a neural network learns from your choices.",
            font_size='20sp',
            font_name='/storage/emulated/0/bin//Roboto-Regular.ttf',
            color=get_color_from_hex('#ecf0f1'),
            halign='center',
            valign='middle'
        )
        about_label.bind(size=about_label.setter('text_size'))
        layout.add_widget(about_label)

        back_button = Button(
            text="Back",
            size_hint=(1, 0.2),
            background_normal='',
            background_color=get_color_from_hex('#e74c3c'),  # قرمز
            color=get_color_from_hex('#ecf0f1'),
            font_size='24sp',
            font_name='/storage/emulated/0/bin/Roboto-Medium.ttf',
            on_release=self.go_back
        )
        layout.add_widget(back_button)

        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.transition = FadeTransition(duration=0.5)
        self.manager.current = 'main_menu'

class SettingsScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_background(get_color_from_hex('#34495e'))  # پس‌زمینه خاکستری تیره
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.sound_toggle = ToggleButton(
            text="Sound: ON",
            size_hint=(1, 0.2),
            background_normal='',
            background_color=get_color_from_hex('#3498db'),  # آبی
            color=get_color_from_hex('#ecf0f1'),
            font_size='24sp',
            font_name='/storage/emulated/0/bin/Roboto-Medium.ttf',
            on_release=self.toggle_sound
        )
        layout.add_widget(self.sound_toggle)

        back_button = Button(
            text="Back",
            size_hint=(1, 0.2),
            background_normal='',
            background_color=get_color_from_hex('#e74c3c'),  # قرمز
            color=get_color_from_hex('#ecf0f1'),
            font_size='24sp',
            font_name='/storage/emulated/0/bin/Roboto-Medium.ttf',
            on_release=self.go_back
        )
        layout.add_widget(back_button)

        self.add_widget(layout)

    def toggle_sound(self, instance):
        if self.sound_toggle.text == "Sound: ON":
            self.sound_toggle.text = "Sound: OFF"
        else:
            self.sound_toggle.text = "Sound: ON"

    def go_back(self, instance):
        self.manager.transition = FadeTransition(duration=0.5)
        self.manager.current = 'main_menu'

class GameScreen(BaseScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_background(get_color_from_hex('#2c3e50'))  # پس‌زمینه آبی تیره
        self.layout = FloatLayout()
        self.add_widget(self.layout)

        self.top_buttons = []
        self.bottom_buttons = []

        # ساخت دکمه‌های 1, 2, 3
        top_row_layout = GridLayout(cols=3, spacing=20, size_hint=(None, None), width=600, height=250)
        for i in range(1, 4):
            btn = Button(
                size_hint=(None, None),
                size=(280, 280),
                background_normal=f'/storage/emulated/0/bin/dikme_{i}.png',
                background_down=f'/storage/emulated/0/bin/buttun_{i}.png',
                on_release=self.make_choice
            )
            self.top_buttons.append(btn)
            top_row_layout.add_widget(btn)

        top_row_layout.pos_hint = {"center_x": 0.384, "center_y": 0.45}
        self.layout.add_widget(top_row_layout)

        # ساخت دکمه‌های 4, 5, 6, 7
        bottom_row_layout = GridLayout(cols=4, spacing=20, size_hint=(None, None), width=1000, height=250)
        for i in range(4, 8):
            btn = Button(
                size_hint=(None, None),
                size=(280, 280),
                background_normal=f'/storage/emulated/0/bin/dikme_{i}.png',
                background_down=f'/storage/emulated/0/bin/button_{i}.png',
                on_release=self.make_choice
            )
            self.bottom_buttons.append(btn)
            bottom_row_layout.add_widget(btn)

        bottom_row_layout.pos_hint = {"center_x": 0.425, "center_y": 0.3}
        self.layout.add_widget(bottom_row_layout)

        # ایجاد Label برای نمایش امتیاز
        self.info_label = Label(
            text="LEVEL: 0",
            font_size="25sp",
            font_name='/storage/emulated/0/bin/Roboto-Bold.ttf',
            color=get_color_from_hex('#ecf0f1'),
            size_hint=(None, None),
            size=(400, 50),
            pos_hint={"center_x": 0.5, "center_y": 0.85}
        )
        self.layout.add_widget(self.info_label)

        # مقداردهی اولیه امتیاز و عدد هدف
        self.score = 0
        self.target_number = random.randint(1, 7)

    def disable_all_buttons(self):
        for btn in self.top_buttons + self.bottom_buttons:
            btn.disabled = True

    def enable_all_buttons(self):
        for btn in self.top_buttons + self.bottom_buttons:
            btn.disabled = False

    def show_game_over_animation(self):
        self.disable_all_buttons()
        Clock.schedule_once(lambda dt: self.create_top_popup(), 0.3)
        Clock.schedule_once(lambda dt: self.create_score_popup(), 0.5)
        Clock.schedule_once(lambda dt: self.create_action_buttons(), 0.8)

    def create_top_popup(self):
        self.top_popup = Image(
            source='/storage/emulated/0/bin/popup_top.png',
            size_hint=(None, None),
            size=(400, 100),
            pos_hint={'center_x': 0.5, 'top': 1.2},
            opacity=0
        )
        anim = Animation(pos_hint={'center_x': 0.5, 'top': 0.8}, opacity=1, duration=0.3, t='out_back')
        self.layout.add_widget(self.top_popup)
        anim.start(self.top_popup)

    def create_score_popup(self):
        self.score_popup = BoxLayout(
            orientation='vertical',
            size_hint=(None, None),
            size=(400, 150),
            pos_hint={'center_x': 0.5, 'top': 0.7},
            opacity=0
        )
        score_label = Label(
            text=f"SCORE: {self.score}",
            font_size='24sp',
            font_name='/storage/emulated/0/bin/Roboto-Bold.ttf',
            color=get_color_from_hex('#2c3e50')
        )
        self.score_popup.add_widget(score_label)
        self.layout.add_widget(self.score_popup)

        anim = Animation(pos_hint={'center_x': 0.5, 'top': 0.6}, opacity=1, duration=0.3, t='out_back')
        anim.start(self.score_popup)

    def create_action_buttons(self):
        self.action_box = BoxLayout(
            orientation='horizontal',
            size_hint=(None, None),
            size=(500, 100),
            pos_hint={'center_x': 0.42, 'top': 0.4},
            opacity=0,
            spacing=20
        )

        again_btn = Button(
            text="AGAIN",
            size_hint=(None, None),
            size=(300,120),
            background_normal='',
            background_color=get_color_from_hex('#2ecc71'),  # سبز
            color=get_color_from_hex('#ecf0f1'),
            font_size='12sp',
            font_name='/storage/emulated/0/bin/Roboto-Medium.ttf',
            on_release=self.reset_game
        )

        menu_btn = Button(
            text="BACK TO MENU",
            size_hint=(None, None),
            size=(390, 120),
            background_normal='',
            background_color=get_color_from_hex('#e74c3c'),  # قرمز
            color=get_color_from_hex('#ecf0f1'),
            font_size='10sp',
            font_name='/storage/emulated/0/bin/Roboto-Medium.ttf',
            on_release=self.back_to_menu
        )

        self.action_box.add_widget(again_btn)
        self.action_box.add_widget(menu_btn)
        self.layout.add_widget(self.action_box)

        anim = Animation(opacity=1, duration=0.3)
        anim.start(self.action_box)

    def reset_game(self, instance):
        for widget in self.layout.children[:]:
            if isinstance(widget, (Image, BoxLayout, FloatLayout)):
                self.layout.remove_widget(widget)

        self.enable_all_buttons()

        self.score = 0
        self.target_number = random.randint(1, 7)
        self.info_label.text = f"LEVEL: {self.score}"

    def back_to_menu(self, instance):
        self.manager.transition = FadeTransition(duration=0.5)
        self.manager.current = 'main_menu'

    def make_choice(self, instance):
        image_path = instance.background_normal
        try:
            choice = int(image_path.split("_")[-1].split(".")[0])
        except ValueError:
            return

        if choice == self.target_number:
            self.info_label.text = f"SCORE: {self.score}"
            self.show_game_over_animation()
        else:
            self.score += 1
            self.target_number = random.randint(1, 7)
            self.info_label.text = f"LEVEL: {self.score}"

class NeuralGameApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(LoadingScreen(name='loading'))
        sm.add_widget(MainMenuScreen(name='main_menu'))
        sm.add_widget(AboutScreen(name='about_screen'))
        sm.add_widget(SettingsScreen(name='settings_screen'))
        sm.add_widget(GameScreen(name='game_screen'))
        return sm

if __name__ == "__main__":
    NeuralGameApp().run()