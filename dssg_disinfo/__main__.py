from .models.run_model import run_model
from .visualization.plot_graphs import plot_graphs

epochs = [2]
if __name__ == "__main__":
    for epoch in epochs:        
        log_file = run_model('basic', epochs=epoch)
        plot_graphs(log_file, 'basic')