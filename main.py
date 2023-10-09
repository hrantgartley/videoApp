from video import Video
import this


def main():
    first = Video(5, 23, "action", "Dexter")
    second = Video(5, 34, "drama", "Breaking Bad")
    third = Video(6, 45, "comedy", "Friends")
    fourth = Video(7, 56, "romance", "The Notebook")
    l_video = [first, second, third, fourth]

    first.print_all(l_video)

    print(this)


if __name__ == "__main__":
    main()
    assert (main() == None)
