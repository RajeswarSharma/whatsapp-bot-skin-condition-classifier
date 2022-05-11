from xml.parsers.expat import model
import cv2 as cv
import PIL.Image as Image
import io
import requests
import numpy
from agents.agentDriver import predictor
lesion_type_dict = {
    'nv': 'Melanocytic nevi (nv)',
    'mel': 'Melanoma (mel)',
    'bkl': 'Benign keratosis-like lesions (bkl)',
    'bcc': 'Basal cell carcinoma (bcc)',
    'akiec': 'Actinic keratoses (akiec)',
    'vasc': 'Vascular lesions (vasc)',
    'df': 'Dermatofibroma (df)'
}
label_mapping = {
    0: 'nv',
    1: 'mel',
    2: 'bkl',
    3: 'bcc',
    4: 'akiec',
    5: 'vasc',
    6: 'df'
}
model_res = 28

def driver(image_url):
    image = pull_resize_image(image_url)
    index = predictor(image)
    return messageGen(index)
    

# Pulling image from twilio url
def pull_resize_image(image_url):
    file = requests.get(image_url).content
    image = Image.open(io.BytesIO(file))
    cvImage = cv.cvtColor(numpy.array(image), cv.COLOR_RGB2BGR)
    cvImage = cv.resize(cvImage,(model_res,model_res),interpolation=cv.INTER_AREA)
    return cvImage

def messageGen(index):
    message =""
    if index == 0:
        message ="*Possible* *Condition*: *Melanocytic* *nevus*\n*Description*: A melanocytic nevus (also known as nevocytic nevus, nevus-cell nevus and commonly as a mole) is a type of melanocytic tumor that contains nevus cells.Some sources equate the term mole with melanocytic nevus,but there are also sources that equate the term mole with any nevus form.\n*Type*: Non-cancerous 🟢"
    elif index ==1:
        message = "*Possible* *Condition*: *Melanoma*\n*Description*: Melanoma, the most serious type of skin cancer, develops in the cells (melanocytes) that produce melanin — the pigment that gives your skin its color. Melanoma can also form in your eyes and, rarely, inside your body, such as in your nose or throat.\n*Type*: Cancerous🔴"
    elif index ==2:
        message = "*Possible* *Condition*:*Seborrheic* *keratosis*\n*Description*:Seborrheic keratosis is a common benign (noncancerous) skin growth. It tends to appear in middle age and you may get more as you get older. Seborrheic keratoses are not pre-cancerous, but they can resemble other skin growths that are.\n*Type*: Non-cancerous 🟢(initially)"
    elif index==3:
        message="*Possible* *Condition*: *Basal* *cell* *carcinoma*\n*Description*: Basal cell carcinoma is a type of skin cancer. Basal cell carcinoma begins in the basal cells — a type of cell within the skin that produces new skin cells as old ones die off. Basal cell carcinoma often appears as a slightly transparent bump on the skin, though it can take other forms. Basal cell carcinoma occurs most often on areas of the skin that are exposed to the sun, such as your head and neck.\n*Type*: Cancerous 🔴"
    elif index ==4:
        message="*Possible* *Condition*: *Actinic* *keratosis*\n*Description*: An actinic keratosis is a rough, scaly patch on the skin that develops from years of sun exposure. It's often found on the face, lips, ears, forearms, scalp, neck or back of the hands. Also known as a solar keratosis, an actinic keratosis grows slowly and usually first appears in people over 40. You can reduce your risk of this skin condition by minimizing your sun exposure and protecting your skin from ultraviolet (UV) rays.\n*Type*: Cancerous 🔴"
    elif index ==5:
        message="*Possibl* *Condition*: *Vascular* *lesions*\n*Description*: Vascular lesions are relatively common abnormalities of the skin and underlying tissues, more commonly known as birthmarks. There are three major categories of vascular lesions: Hemangiomas, Vascular Malformations, and Pyogenic Granulomas. While these birthmarks can look similar at times, they each vary in terms of origin and necessary treatment.\n*Type*: possibly cancerous 🟠"
    else:
        message ="*Possible* *Condition*: *Dermatofibroma* \n*Description*: Dermatofibroma (superficial benign fibrous histiocytoma) is a common cutaneous nodule of unknown etiology that occurs more often in women. Dermatofibroma frequently develops on the extremities (mostly the lower legs) and is usually asymptomatic, although pruritus and tenderness can be present. It is actually the most common painful skin tumor.\n*Type*: Cancerous 🔴"
    return message