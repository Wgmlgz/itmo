from utils import normalize
import pytesseract
import cv2 as cv
import numpy as np
from pprint import pprint


def parse():
    filename = 'img.png'
    img = cv.imread(cv.samples.findFile(filename))
    img_h = 500
    img_w = 500
    dim = (img_h, img_w)

    img = cv.resize(img, dim, interpolation=cv.INTER_LINEAR)

    cImage = np.copy(img)  # image to draw lines
    # cv.imshow("image", img) #name the window as "image"
    # cv.waitKey(0)
    # cv.destroyWindow("image") #close the window
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # cv.imshow("gray", gray)
    # cv.waitKey(0)
    # cv.destroyWindow("gray")
    canny = cv.Canny(gray, 10, 150)
    # cv.imshow("canny", canny)
    # cv.waitKey(0)
    # cv.destroyWindow("canny")

    # cv.HoughLinesP(image, rho, theta, threshold[, lines[, minLineLength[, maxLineGap]]]) → lines
    rho = 1
    theta = np.pi/180
    threshold = 50
    minLinLength = 350
    maxLineGap = 6
    linesP = cv.HoughLinesP(canny, rho, theta, threshold,
                            None, minLinLength, maxLineGap)

    def is_vertical(line):
        return line[0] == line[2]

    def is_horizontal(line):
        return line[1] == line[3]

    horizontal_lines = []
    vertical_lines = []

    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            if (is_vertical(l)):
                vertical_lines.append(l)

            elif (is_horizontal(l)):
                horizontal_lines.append(l)
    for i, line in enumerate(horizontal_lines):
        cv.line(cImage, (line[0], line[1]),
                (line[2], line[3]), (0, 255, 0), 3, cv.LINE_AA)

    for i, line in enumerate(vertical_lines):
        cv.line(cImage, (line[0], line[1]),
                (line[2], line[3]), (0, 0, 255), 3, cv.LINE_AA)

    # cv.imshow("with_line", cImage)
    # cv.waitKey(0)
    # cv.destroyWindow("with_line") #close the window

    def overlapping_filter(lines, sorting_index):
        filtered_lines = []

        lines = sorted(lines, key=lambda lines: lines[sorting_index])
        separation = 5
        for i in range(len(lines)):
            l_curr = lines[i]
            if (i > 0):
                l_prev = lines[i-1]
                if ((l_curr[sorting_index] - l_prev[sorting_index]) > separation):
                    filtered_lines.append(l_curr)
            else:
                filtered_lines.append(l_curr)

        return filtered_lines

    horizontal_lines = []
    vertical_lines = []

    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            if (is_vertical(l)):
                vertical_lines.append(l)

            elif (is_horizontal(l)):
                horizontal_lines.append(l)
        horizontal_lines = overlapping_filter(horizontal_lines, 1)
        vertical_lines = overlapping_filter(vertical_lines, 0)
    for i, line in enumerate(horizontal_lines):
        cv.line(cImage, (line[0], line[1]),
                (line[2], line[3]), (0, 255, 0), 3, cv.LINE_AA)
        cv.putText(cImage, str(i) + "h", (line[0] + 5, line[1]),
                   cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv.LINE_AA)
    for i, line in enumerate(vertical_lines):
        cv.line(cImage, (line[0], line[1]),
                (line[2], line[3]), (0, 0, 255), 3, cv.LINE_AA)
        cv.putText(cImage, str(i) + "v", (line[0], line[1] + 5),
                   cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv.LINE_AA)

    # cv.imshow("with_line", cImage)
    # cv.waitKey(0)
    # cv.destroyWindow("with_line")  # close the window

    # set keywords
    keywords = ['no', 'kabupaten', 'kb_otg', 'kl_otg', 'sm_otg', 'ks_otg', 'not_cvd_otg',
                'kb_odp', 'kl_odp', 'sm_odp', 'ks_odp', 'not_cvd_odp', 'death_odp',
                'kb_pdp', 'kl_pdp', 'sm_pdp', 'ks_pdp', 'not_cvd_pdp', 'death_pdp',
                'positif', 'sembuh', 'meninggal']

    dict_kabupaten = {}
    for keyword in keywords:
        dict_kabupaten[keyword] = []

    # set counter for image indexing
    counter = 0

    # set line index
    first_line_index = 1
    last_line_index = 5

    def get_cropped_image(image, x, y, w, h):
        cropped_image = image[y:y+h, x:x+w]
        return cropped_image

    def get_ROI(image, horizontal, vertical, left_line_index, right_line_index, top_line_index, bottom_line_index, offset=4):
        x1 = vertical[left_line_index][2] + offset
        y1 = horizontal[top_line_index][3] + offset

        try:
            x2 = vertical[right_line_index][2] - offset
        except:
            x2 = img_w

        try:
            y2 = horizontal[bottom_line_index][3] - offset
        except:
            y2 = img_h

        w = x2 - x1
        h = y2 - y1

        cropped_image = get_cropped_image(image, x1, y1, w, h)

        return cropped_image, (x1, y1, w, h)

    # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

    def draw_text(src, x, y, w, h, text):
        cFrame = np.copy(src)
        cv.rectangle(cFrame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv.putText(cFrame, "text: " + text, (50, 50),
                   cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 5, cv.LINE_AA)

        return cFrame

    def detect(cropped_frame, is_number=False):
        if (is_number):
            text = pytesseract.image_to_string(cropped_frame,
                                               config='-c tessedit_char_whitelist=0123456789 --psm 10 --oem 2')
        else:
            text = pytesseract.image_to_string(
                cropped_frame, config='--psm 10')

        return text

    counter = 0
    print("Start detecting text...")
    (thresh, bw) = cv.threshold(gray, 200, 255, cv.THRESH_BINARY)

    # cv.imshow("with_line", bw)
    # cv.waitKey(0)
    # cv.destroyWindow("with_line")
    arr = []
    for i in range(1, len(horizontal_lines)):
        t = []
        for j in range(1, len(vertical_lines)):
            # for j, keyword in enumerate(keywords):
            counter += 1

            left_line_index = j
            right_line_index = j+1
            top_line_index = i
            bottom_line_index = i+1

            cropped_image, (x, y, w, h) = get_ROI(bw, horizontal_lines, vertical_lines,
                                                  left_line_index, right_line_index, top_line_index, bottom_line_index)
            if w < 5 or h < 5:
                continue
            # text = detect(cropped_image)
            # if (keywords[j]=='kabupaten'):
            #    text = detect(cropped_image)
            #    dict_kabupaten[keyword].append(text)

            # else:
            text = detect(cropped_image, is_number=True)
            text = str(text).strip()

            if text == '':
                text = None
            else:
                text = int(str(text).strip())
            print('{:>5}'.format(str(text)), end='')
            t.append(text)
            #     dict_kabupaten[keyword].append(text)
            # image_with_text = draw_text(img, x, y, w, h, text)
            # cv.imshow("with_line", image_with_text
            #           )
            # cv.waitKey(0)
            # cv.destroyWindow("with_line") #close the window
        arr.append(t)
        print('')
    if len(arr[-1]) == 0:
        arr.pop()

    pprint(arr)
    return arr


if __name__ == '__main__': 
    parse()