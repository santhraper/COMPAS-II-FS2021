from compas.geometry import Frame
from compas.geometry import Transformation
from compas.geometry import Box,Point,Vector,Plane
from compas_rhino.artists import FrameArtist
from compas_rhino.artists import BoxArtist
from compas_rhino.artists import MeshArtist
from compas.datastructures import Mesh
from compas.geometry import Projection


# Frame F representing a coordinate system
F = Frame([6, 6, 7], [2, 3, 5], [2, 6, 7])
width, length, height = 3, 3, 3
box = Box(F, width, length, height)

# Create a Projection (orthogonal)
plane = ((1,4,0), (0,0,1))
P = Projection.from_plane(plane)

# Create a Projection ( parallel)
#point = [0, 0, 0]
#normal = [0, 0, 1]
#plane = Plane(point, normal)
#direction = [1, 1, 1]
#P = Projection.from_plane_and_direction(plane, direction)

# Create a Projection ( perspective)
#center_of_projection = [1, 1, 0]
#P = Projection.from_plane_and_point(plane, center_of_projection)

# Create a Mesh from the Box
mesh = Mesh.from_shape(box)

# Transform Mesh
#T = Transformation.from_frame_to_frame( Frame.worldXY(),F)

#mesh_transformed = mesh.transformed(T)

#Apply projection to mesh
mesh_projected = mesh.transformed(P)




# create artists
#artist1 = FrameArtist(Frame.worldXY())
artist2 = BoxArtist(box)
#artist3 = FrameArtist(F)
artist5 = MeshArtist(mesh_projected)

#Draw

#artist3.draw()
artist2.draw()
artist5.draw_edges(color="#fff000")