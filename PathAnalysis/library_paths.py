def init(context):
    ExtAPI.Log.WriteMessage("Initialize Linearized Results path library...")

def create_shortest_path(analysis):

    # Specify unit
    ExtAPI.Application.ActiveUnitSystem = MechanicalUnitSystem.StandardNMM
    
    # Retrieve Starting Node for Path
    meshData = DataModel.AnalysisList[0].MeshData
    N1 = meshData.NodeById(DataModel.GetObjectsByName("Path_Node")[0].Location.Ids[0])

    # Retrieve Surface
    Sid = DataModel.GetObjectsByName("Path_Surface")[0].Location
    S=meshData.MeshRegionById(Sid.Ids[0])

    # Find Surface Node that has shortest distance to Starting Node
    D=0
    for NId in S.NodeIds:
        Ni = meshData.NodeById(NId)
        if D==0: 
            D = sqrt(pow((N1.X-Ni.X),2)+pow((N1.Y-Ni.Y),2)+pow((N1.Z-Ni.Z),2))
            N2 = Ni

        elif D > sqrt(pow((N1.X-Ni.X),2)+pow((N1.Y-Ni.Y),2)+pow((N1.Z-Ni.Z),2)):
            D = sqrt(pow((N1.X-Ni.X),2)+pow((N1.Y-Ni.Y),2)+pow((N1.Z-Ni.Z),2))
            N2 = Ni
            
        else:
            pass

    # Initialize Path creation
    construction_geometry_1 = Model.AddConstructionGeometry()
    
    # Define Starting Node for Path
    path_1 = construction_geometry_1.AddPath()
    path_1.StartXCoordinate = Quantity(N1.X, "m")
    path_1.StartYCoordinate = Quantity(N1.Y, "m")
    path_1.StartZCoordinate = Quantity(N1.Z, "m")
    
    # Define Ending Node for Path
    path_1.EndXCoordinate = Quantity(N2.X, "m")
    path_1.EndYCoordinate = Quantity(N2.Y, "m")
    path_1.EndZCoordinate = Quantity(N2.Z, "m")