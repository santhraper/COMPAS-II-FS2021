from compas.geometry import Frame
from compas.geometry import Transformation
from compas.geometry import Box,Point,Vector,Plane
from compas_rhino.artists import FrameArtist
from compas_rhino.artists import BoxArtist
from compas_rhino.artists import MeshArtist
from compas.datastructures import Mesh
from compas.geometry import Projection





# Frame F representing a coordinate system
F = Frame([10, 10, 2], [-2, 3, -2], [-2, 4, -2])
width, length, height = 3, 5, 5
box = Box(F, width, length, height)



# Create a Projection (can be orthogonal, parallel or perspective)
plane = Plane([0,0,0], [0,0,1])
P = Projection.from_plane(plane)

# Create a Mesh from the Box
mesh = Mesh.from_shape(box)
# Get transformation between world and frame F
T = Transformation.from_frame_to_frame( Frame.worldXY(),F)

# Apply transformation on box.
mesh_projected = mesh.transformed(T)

# create artists
artist1 = FrameArtist(Frame.worldXY())
artist2 = BoxArtist(box)
artist3 = FrameArtist(F)
artist5 = MeshArtist(mesh_projected)

#Draw

artist3.draw()
artist2.draw()
artist5.draw_edges(color="#ffff00")