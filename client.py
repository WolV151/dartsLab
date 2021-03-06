import logging
import grpc
import darts_match_pb2
import darts_match_pb2_grpc
from datatype.enums import DartMultiplier

def run():
    channel = grpc.insecure_channel('localhost:50055')
    
    stub = darts_match_pb2_grpc.DartsMatchStub(channel)

    match1 = stub.CreateMatch(darts_match_pb2.MatchRequest(userName='Alice', matchType = 'X01')).matchId
    m1_player1 = 0
    m1_player2 = stub.RegisterPlayer(darts_match_pb2.RegisterRequest(matchId=match1, userName = 'Jamal')).playerIndex
    stub.FinalizeMatch(darts_match_pb2.FinalizeRequest(matchId=match1))

    match2 = stub.CreateMatch(darts_match_pb2.MatchRequest(userName='Bobby', matchType = 'X01')).matchId
    m2_player1 = 0
    m2_player2 = stub.RegisterPlayer(darts_match_pb2.RegisterRequest(matchId=match1, userName = 'Norris')).playerIndex
    stub.FinalizeMatch(darts_match_pb2.FinalizeRequest(matchId=match2))

    my_visit = [
        darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=1),
        darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=5),
        darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=20),
    ]
    
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(matchId=match1, playerIndex=m1_player1, visit=my_visit))
    print(response.message)

    my_visit = [
        darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=1),
        darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=15),
        darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=20),
    ]
    
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(matchId=match2, playerIndex=m2_player1, visit=my_visit))
    print(response.message)

    my_visit = [
        darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=1),
        darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=5),
        darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=20),
    ]
    
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(matchId=match1, playerIndex=m1_player1, visit=my_visit))
    print(response.message)

    my_visit = [
        darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20),
        darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=5),
        darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=2),
    ]
    
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(matchId=match1, playerIndex=m1_player2, visit=my_visit))
    print(response.message)

    my_visit = [
        darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=10),
        darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=5),
        darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=20),
    ]
    
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(matchId=match1, playerIndex=m1_player1, visit=my_visit))
    print(response.message)

    my_visit = [
        darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=1),
        darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=20),
        darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=20),
    ]
    
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(matchId=match1, playerIndex=m1_player2, visit=my_visit))
    print(response.message)

    my_visit = [
        darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=1),
        darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20),
        darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20),
    ]
    
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(matchId=match2, playerIndex=m2_player2, visit=my_visit))
    print(response.message)

if __name__ == "__main__":
    logging.basicConfig()
    run()