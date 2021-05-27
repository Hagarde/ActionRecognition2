 from params import * 
 from keras.preprocessing.image import smart_resize
 
 def load_video(camera) :                                        #la longueur de chaque vidéo est différente donc il faudrait fixer une longueur max pour le dataloader
    L=[]
    ret = True 
    while ret : 
        ret, frame = camera.read()
        frame = smart_resize(np.asarray(frame), self.image_size)                
        L.append(frame)
    return L 