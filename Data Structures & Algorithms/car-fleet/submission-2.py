class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = []

        cars = list(zip(position, speed))
        cars.sort(key=lambda x: x[0], reverse=True)

        for pos, spd in cars:
            time = (target-pos) / spd
            if not times:
                times.append(time)
                continue
            if times:
                if time > times[-1]:
                    times.append(time)
                elif time == times[-1]:
                    times.pop()
                    times.append(time)

        return len(times)