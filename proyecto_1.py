from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.listview import ListView, ListAdapter
from kivy.uix.label import Label
import os


class MusicApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical')
        self.label = Label(text='Buscando canciones...')
        self.root.add_widget(self.label)

        # Buscar archivos de música en el almacenamiento
        self.music_files = self.scan_music_files("/storage/emulated/0/Music")

        if not self.music_files:
            self.label.text = "No se encontraron canciones."
        else:
            self.label.text = "Selecciona una canción:"

            # Crear lista de canciones
            song_buttons = [Button(text=song, size_hint_y=None, height=40) for song in self.music_files]

            for btn in song_buttons:
                btn.bind(on_press=self.play_song)
                self.root.add_widget(btn)

        return self.root

    def scan_music_files(self, directory):
        extensions = ['.mp3', '.wav', '.ogg', '.flac', '.m4a']
        music_files = []

        for root, dirs, files in os.walk(directory):
            for file in files:
                if any(file.endswith(ext) for ext in extensions):
                    music_files.append(file)

        return sorted(music_files)

    def play_song(self, instance):
        print(f"Reproduciendo: {instance.text}")  # Aquí agregaremos la funcionalidad de reproducción


if __name__ == "__main__":
    MusicApp().run()
