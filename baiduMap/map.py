"""
Base Map Render
http://lbsyun.baidu.com/
"""
from jinja2 import Environment, FileSystemLoader
def init():
    '''
    Initialize baidu map construction class, must be used before use, otherwise may throw NameError
    '''
    global environment
    environment = Environment(loader=FileSystemLoader('map_template'))


class Map(object):
    """
    Render Map

    Parameters
    ----------
    ak: Baidu Map AK

    title: Page:Title
    center_pos:Center Coordinates
    level:Zoom Level
    open_zoom:Is Open Zoom(True|False)
    tilt:Map Tilt Degree
    is_has_scaleControl:Defined is/isn't have ScaleControl Widget
    is_has_zoomControl:Defined is/isn't have ZoomControl
    encoding:HTML Encoding




    >>> init()
    >>> a = Map("xxx", title="Hello World", center_pos=[112.924018, 28.227352])
    >>> a.new_point(116.43244,39.914714)
    >>> a.render("a.html")
    """
    def __init__(self,ak: str, title: str="Map",center_pos:list=[116.404, 39.915],level:int=15,open_zoom: bool=True,
                 tilt:int=0,
               is_has_scaleControl:bool=True,is_has_zoomControl:bool=True, encoding: str="utf-8"):

        self.ak=ak
        self.title=title
        self.center_pos=center_pos
        self.level=level
        self.open_zoom=open_zoom
        self.tilt=tilt
        self.is_has_scaleControl=is_has_scaleControl
        self.is_has_zoomControl=is_has_zoomControl
        self.encoding=encoding
        self.point_pos_list=[]

    def new_point(self,lon,lat):
        '''
         New A Point Dot

        Parameters
        ----------
        lon : float
            Longitude
        lat : float
            Latitude

        Returns
        -------
        None


        '''
        pos=",".join([str(lon),str(lat)])
        self.point_pos_list.append(pos)
    def render(self,output):
        '''
         New A Point Dot

        Parameters
        ----------
        output:Output File Dir

        Returns
        -------
        True

        Returns Type
        ------------
        bool

        '''
        template=environment.get_template("basic.html")
        content = template.render(ak=self.ak , title=self.title,lon=str(self.center_pos[0]),lat=str(self.center_pos[1]),level=self.level,open_zoom=self.open_zoom,tilt=self.tilt,
                              is_has_scaleControl=self.is_has_scaleControl,is_has_zoomControl=self.is_has_zoomControl,
                              point_pos_list=self.point_pos_list)
        with open(output, "w", encoding=self.encoding) as f:
            f.write(content)
        return True


# map=Map("GKbp3EUF40Fl1It6adMdFMfIzsvFz83a")

