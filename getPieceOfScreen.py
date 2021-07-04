import mss
def main():
    with mss.mss() as sct:
        # Part of the screen to capture
        monitor = {"top": 345, "left": 0, "width": 640, "height": 468}
        while True:
            # Get raw pixels from the screen, save it to a Numpy array
            frame = np.array(sct.grab(monitor))

            if cv.waitKey(1) & 0xFF == ord('q'):
                break

if __name__ == '__main__':
    main()
