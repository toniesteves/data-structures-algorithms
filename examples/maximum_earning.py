# Maximum Earning
#
# a taxi driver knows the pick-up and drop-off locations of people who are requesting taxi services. All the locations
# are in km from the starting point. The starting point is 0km. For each km travelled by a passenger, the driver charges
# 1 unit of money per passenger. Moreover the taxi itself is very fancy. Therefore some people are even willing to pay
# extra tip if they get to travel in the taxi. At any point of time the taxi can accommodate only one passenger.
# Determine the maximum amount the driver can earn.


def max_taxi_earning(pickup, drop, tip):
    # Ordenar as corridas pelo destino
    rides = [(pickup[i], drop[i], tip[i]) for i in range(len(pickup))]

    rides.sort(key=lambda x: x[1])  # x[1] = destino

    # Criar lista de destinos para busca manual
    destinations = [ride[1] for ride in rides]

    # DP: dp[i] representa o máximo ganho até a corrida i
    dp = [0] * len(rides)

    for i in range(len(rides)):
        start, end, tip = rides[i]
        profit = (end - start) + tip

        # Encontrar manualmente a última corrida que não conflita
        idx = -1
        for j in range(i - 1, -1, -1):  # Iterar de trás para frente
            if rides[j][1] <= start:
                idx = j
                break

        if idx != -1:
            profit += dp[idx]  # Somar o melhor lucro obtido até essa corrida não conflitante

        dp[i] = max(dp[i - 1], profit) if i > 0 else profit  # Melhor escolha entre pegar ou não a corrida

    return dp[-1] if dp else 0


# Exemplo de uso

pickup = [0, 2, 9, 10, 11, 12]
drop   = [5, 9, 11, 11, 14, 17]
tip    = [1, 2 , 3 , 2 , 2 ,1]

print(max_taxi_earning(pickup, drop, tip))