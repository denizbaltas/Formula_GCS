import numpy as np

def plot_speed_profile(ax, s, speed):
    
    #s: pist konumu
    #speed: araç hızı
    

    ax.plot(s, speed, color='dimgray', linewidth=1.5, alpha=0.7)

    ax.axhline(np.mean(speed), color='gray', linestyle='--', linewidth=1, alpha=0.5)

    #High speed region GREEN
    ax.fill_between(
        s, speed, np.mean(speed),
        where=(speed >= np.mean(speed)),
        color='green', alpha=0.3, interpolate=True,
        label='High Speed'
    )

    #Low speed region RED
    ax.fill_between(
        s, speed, np.mean(speed),
        where=(speed < np.mean(speed)),
        color='red', alpha=0.3, interpolate=True,
        label='Low Speed'
    )

    ax.set_title("Speed Profile")
    ax.set_xlabel("Distance [s]")
    ax.set_ylabel("Speed [km/h]")
    ax.grid(True)
    ax.legend(loc='upper right')