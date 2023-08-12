import cv2
import dlib

Cap = cv2.VideoCapture("video.mp4")
Trackers=[]
while True:
    Rec, Frames= Cap.read()
    
    Frames = cv2.resize(Frames,(800,480))
    rgb_Frame = cv2.cvtColor(Frames,cv2.COLOR_BGR2RGB)
    
    
    for Tracker in Trackers:
        Tracker.update(rgb_Frame)
        Position=Tracker.get_position()
        x1=int(Position.left())
        y1=int(Position.top())
        x2=int(Position.right())
        y2=int(Position.bottom())
        
        cv2.rectangle(Frames,(x1,y1),(x2,y2),(0,255,0,2),3)
        
        Locate_Text = (int(x1)), (int(y1 - 30))
        Text = "OBJECT TRACKED IN [{}, {}]".format(x1, y2)
        cv2.putText(Frames, Text, Locate_Text, cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 255), 1)

    
    t=cv2.waitKey(30)
    if t == ord('S') or t== ord('s'):
        Rois=cv2.selectROIs("VIDEO",Frames,showCrosshair=True,fromCenter=False)  
        
        for Roi in Rois:
            x1,y1,width,height=Roi
            x2=x1+width
            y2=y1+height
            
            Tkr=dlib.correlation_tracker()
            Rect=dlib.rectangle(x1,y1,x2,y2)
            Tkr.start_track(rgb_Frame,Rect)
            Trackers.append(Tkr)
    
    cv2.imshow("VIDEO",Frames)
            
    if t == ord('Q')or t== ord('q'):
        break

    
Cap.release()
cv2.destroyAllWindows()