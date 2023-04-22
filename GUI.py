from tkinter import *
from tkinter import ttk
from PIL import ImageTk

from validation import validate_threshold_value, validate_softness_white


class GUI:
    def __init__(self, size, title):
        self.root = Tk()
        self.configurate_window(size, title)

        self.threshold_value = StringVar(value='0.8')
        self.softness_white = StringVar(value='100')

        self.groups_frame = None

        self.main_frame = ttk.Frame(self.root, padding='3 3 12 12')
        self.configurate_main_frame()
        self.draw_ui()

    def configurate_window(self, size, title):
        self.root.title(title)
        self.root.geometry(size)

    def configurate_main_frame(self):
        self.main_frame.grid(column=0, row=0, columnspan=12, rowspan=12)

    def draw_ui(self):
        self.show_config()

    def show_config(self):
        config_frame = ttk.Frame(self.main_frame)
        config_frame.grid(column=0, row=0)

        threshold_value_label = ttk.Label(config_frame, text='Пороговое значение:', font=14)
        threshold_value_label.grid(column=0, row=0, columnspan=1, rowspan=1)

        validate_threshold_value_wrapper = (self.root.register(validate_threshold_value), '%P')
        threshold_value_entry = ttk.Entry(config_frame, textvariable=self.threshold_value, validate='key', validatecommand=validate_threshold_value_wrapper)
        threshold_value_entry.grid(column=1, row=0, columnspan=1, rowspan=1)

        softness_white_label = ttk.Label(config_frame, text='Мягкость белого:', font=14)
        softness_white_label.grid(column=0, row=1, columnspan=1, rowspan=1, sticky='w')

        softness_white_value_wrapper = (self.root.register(validate_softness_white), '%P')
        softness_white_entry = ttk.Entry(config_frame, textvariable=self.softness_white, validate='key', validatecommand=softness_white_value_wrapper)
        softness_white_entry.grid(column=1, row=1, columnspan=1, rowspan=1)
        #
        # self.run_art_btn = ttk.Button(config_frame, text='Обработать изображения')
        # self.run_art_btn.grid(column=0, row=2)

    def show_raw_images(self, images):
        raw_images_frame = ttk.Frame(self.main_frame)
        raw_images_frame.grid(column=0, row=1, sticky='w')
        self.show_images(raw_images_frame, 'Иконки до бинаризации', images)

    def show_bin_images(self, images):
        bin_images_frame = ttk.Frame(self.main_frame)
        bin_images_frame.grid(column=0, row=2, sticky='w')
        self.show_images(bin_images_frame, 'Иконки после бинаризации', images)
        
    def show_art_groups(self, groups, images):
        self.groups_frame = ttk.Frame(self.main_frame, name='groups')
        self.groups_frame.grid(column=0, row=3, sticky='w')

        groups_images = {}
        for i in range(len(groups)):
            groups_images.setdefault(groups[i], []).append(images[i])

        for i, images_list in enumerate(groups_images):
            group_label = ttk.Label(self.groups_frame, text=f'Кластер {i}')
            group_label.grid(column=i, row=0)

            for j, image in enumerate(groups_images[images_list]):
                image = ImageTk.PhotoImage(image)
                image_label = ttk.Label(self.groups_frame, image=image)
                image_label.image = image
                image_label.grid(column=i, row=j + 1, sticky='w')

    def clear_art_groups(self):
        if self.groups_frame:
            self.groups_frame.destroy()

    def show_images(self, frame, title, images):
        title_label = ttk.Label(frame, text=title)
        title_label.grid(column=0, row=0, sticky='w')

        for i, bin_image in enumerate(images):
            image = ImageTk.PhotoImage(bin_image)
            image_label = ttk.Label(frame, image=image)
            image_label.image = image
            image_label.grid(column=i, row=1, sticky='w')

    def mainloop(self):
        self.root.mainloop()
