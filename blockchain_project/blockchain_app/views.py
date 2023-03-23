from django.shortcuts import render
from django.http import JsonResponse
from .blockchain import Blockchain

def mine_block(request):
    if request.method == 'POST':
        sender = request.POST.get('sender')
        recipient = request.POST.get('recipient')
        amount = float(request.POST.get('amount'))

        blockchain = Blockchain()
        transaction = blockchain.create_transaction(sender, recipient, amount)
        block = blockchain.mine_block()

        response_data = {
            'message': 'New block mined!',
            'block': {
                'id': block.id,
                'hash': block.hash,
                'timestamp': block.timestamp,
                'previous_hash': block.previous_hash,
                'transactions': [t.__str__() for t in block.transactions.all()]
            },
            'transaction': transaction.__str__()
        }
        return JsonResponse(response_data)
    
    return render(request, 'mine_block.html')


from django.shortcuts import render
from .models import Block, Transaction

def blockchain_explorer(request):
    blocks = Block.objects.all()
    transactions = Transaction.objects.all()
    context = {
        'blocks': blocks,
        'transactions': transactions,
    }
    return render(request, 'index.html', context)
