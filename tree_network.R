library(igraph)
library(readr)

adjacency_matrix_plot1 <- read_csv("datasets/adjacency_matrix_plot1.csv")
Plot1_Tree_Data <- read_csv("datasets/Plot1_Tree_Data.csv")

adjacency_matrix_plot1 = adjacency_matrix_plot1[,-1]
node_layout = data.matrix(Plot1_Tree_Data[,-1])

g = graph_from_adjacency_matrix(
  data.matrix(adjacency_matrix_plot1),
  mode = c("undirected"),
  weighted = NULL,
  diag = TRUE,
  add.colnames = NULL,
  add.rownames = NA
)

plot(g, layout = node_layout)
