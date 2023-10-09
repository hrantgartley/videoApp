

class Video:
    def __init__(self, rating=0, length=0, genre="", title=""):
        self.rating = rating
        self.length = length
        self.genre = genre
        self.title = title
        self.videos = []

    def __str__(self) -> str:
        return (
            f"Video rating: {self.rating}\n"
            f"Video length: {self.length}\n"
            f"Video genre: {self.genre}\n"
            f"Video title: {self.title}\n"
        )

    def set_rating(self, rating):
        self.rating = rating

    def get_rating(self):
        return self.rating

    def set_length(self, length):
        self.length = length

    def get_length(self):
        return self.length

    def set_genre(self, genre):
        self.genre = genre

    def get_genre(self):
        return self.genre

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def class_main(self):
        return self.length * self.rating

    def verify_length(self):
        if self.length < 0:
            return abs(self.length)
        else:
            return True

    def add_video(self, rating, length, genre, title):
        new_video = Video(rating, length, genre, title)
        return self.videos.append(new_video)

    def remove_video(self, rating, length, genre, title):
        video_to_remove = Video(rating, length, genre, title)
        return self.videos.remove(video_to_remove)

    def print_all(self, videos):
        for i, video in enumerate(videos):
            print(f"Video {i + 1}\n{video}")
        return

    def print_by_genre(self, videos, genre):
        for iter, video in enumerate(videos):
            if video.genre == genre:
                print(f"{iter + 1}\n{video}")
        return

    def print_by_name(self, videos, title):
        for iter, video in enumerate(videos):
            if video.title == title:
                print(f"{iter + 1}\n{video}")
        return

    def print_by_rating(self, videos, rating):
        for i, video in enumerate(videos):
            if video.rating == rating:
                print(f"Video {i+1}\n{video}")
        return

    def sort_by_rating(self, videos):
        return sorted(
            videos,
            key=lambda x: x.rating
        )

    def sort_by_length(self, videos):
        return sorted(
            videos,
            key=lambda x: x.length
        )
