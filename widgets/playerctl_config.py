from subprocess import CompletedProcess, run

class Data:
    title:str
    artist:str
    current_duration:str
    total_duration:str
    album:str
    time_remaining:str

    def __init__(self, title:str, artist:str, current_duration:str, total_duration:str, album:str, time_remaining:str) -> None:
        self.title = title
        self.artist = artist
        self.current_duration = current_duration
        self.total_duration = total_duration
        self.album = album
        self.time_remaining = time_remaining
        
    def __str__(self) -> str:
            return (f"Title: {self.title}\n"
                    f"Artist: {self.artist}\n"
                    f"Current Duration: {self.current_duration}\n"
                    f"Total Duration: {self.total_duration}\n"
                    f"Album: {self.album}\n"
                    f"Time Remaining: {self.time_remaining}")

def list_mapper(data_list:list) -> Data:
    return Data(title=data_list[0], artist=data_list[1], current_duration=data_list[2], total_duration=data_list[3], album=data_list[4], time_remaining=data_list[5])

class PlayerCtl():
    def get_current_metadata(self) -> Data:
        command: str = "playerctl metadata -f '{{title}}/{{artist}}/{{duration(position)}}/{{duration(mpris:length)}}/{{album}}/{{ duration(mpris:length - position) }}' 2>/dev/null"
        
        proc: CompletedProcess = run(
            command,
            shell=True,
            capture_output=True
        )


        output:str = proc.stdout.decode().strip()

        metadata:list = output.split('/')
        if len(metadata) != 6:
            return Data(
                title="",
                artist="",
                current_duration="0:00",
                total_duration="0:00",
                album="loading...",
                time_remaining="0:00"
            )

        return list_mapper(metadata) 
    