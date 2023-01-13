import os
from PIL import Image, ImageOps
from roboflow import Roboflow
import shutil


def detectCar(photo):
  rf = Roboflow(api_key="uVh1ZaN4grG0vlIcT9iX")
  project = rf.workspace().project("collectiondata-final")
  model = project.version(1).model
  try:
    prediction = model.predict(photo, confidence=40, overlap=30).predictions[0]
    return prediction["x"], prediction["y"], prediction["width"], prediction["height"]
  except:
    print("\nNo se ha reconocido un auto, usando mascara sin recortar imagen")
    ancho, alto = Image.open(photo).size
    return ancho/2, alto/2, ancho, alto


def getMargins(x, y, w, h, autoSize):
  xMargin = (w/2) + 100
  yMargin = (h/2) + 100
  while True:
    if (x+xMargin <= autoSize[0] and x-xMargin >= 0):
      break
    xMargin -= 10

  while True:
    if (y+yMargin <= autoSize[1] and y-yMargin >= 0):
      break
    yMargin -= 10

  return xMargin, yMargin

def useMask():
  mask = Image.open("mascara.png")
  mask = mask.resize((960, 960))
  if not( os.path.exists("process")):
    os.mkdir("process")
  else:
    for file in os.listdir("process"):
      os.remove("process/" + file)
  for patente in os.listdir("input"):
    if not (os.path.exists('output/' + patente)):
        os.mkdir('output/' + patente)
    else:
      for file in os.listdir('output/' + patente):
        os.remove('output/' + patente + "/" + file)
    i=0
    for photo in os.listdir("input/" + patente):
      background = Image.open("White_Background.jpg")
      background = background.resize((960, 960))
      try:
        auto = Image.open("input/" + patente + "/" + photo).convert("RGBA")
        auto = ImageOps.exif_transpose(auto)
      except:
        print("Error al abrir " + patente + "/" + photo + ". Archivo no es una imagen o está corrupta\n")
        continue
      auto.thumbnail((960, 960), Image.LANCZOS)
      route = "process/car"+ str(i) + ".png"
      auto.save(route)
      x, y, w, h = detectCar(route)
      auto = Image.open(route)
      xMargin, yMargin = getMargins(x, y, w, h, auto.size)
      car = auto.crop((x-xMargin, y-yMargin, x+xMargin, y+yMargin))
      car = car.resize((960, int((car.size[1]/car.size[0])*960)))
      if xMargin > yMargin:
        Image.Image.paste(background, car, (0, 960-car.size[1]))
        Image.Image.paste(background, mask, mask=mask)
      else:
        Image.Image.paste(car, mask, (0, car.size[1]-960), mask)

      background = background.crop((0, 960-car.size[1], 960, 960))
      background.save('output/' + patente + "/" + photo)
      print("\nCompletado", photo, "\n")
      i+=1
    for file in os.listdir("process"):
      os.remove("process/" + file)
    print("Completado", patente, "\n")



useMask()
shutil.rmtree("process")
print("Terminando ejecucion")
