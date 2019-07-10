from  pynput.mouse import Listener


#after add temp counter for rhythm
def on_click(x,y,button,pressed):
    print('mouse pressed')
    


with Listener(on_click = on_click) as listener:
    listener.join()
    
