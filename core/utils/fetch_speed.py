import speedtest


def get_speed():
    st = speedtest.Speedtest()
    st.get_best_server()

    return st.results.ping, (round(st.download() / 1000 / 1000, 1)), (round(st.upload() / 1000 / 1000, 1))