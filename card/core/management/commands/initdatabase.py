# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.utils import timezone

from card.core.models import InitDatabaseLog
from card.models import User, DefaultMessages


class Command(BaseCommand):
    args = '<no_arguments ...>'
    help = 'Init Database for new environment'

    def handle(self, *args, **options):
        init_db(self, "default_user_init")
        init_db(self, "default_message_init")
        init_db(self, "register_invited_persons")
        init_db(self, "register_default_messages")

        self.stdout.write('Succesfully Init Database')


def register_default_messages():
    default_user = User.objects.get(name=u'형정석', last_number=u'2857')

    message_list = {}

    message_list['money'] = [
        u'축의금 보내주시려구요?',
        u'굳이 이렇게라도 보내주시겠다면..',
        u'01092142857 우리은행 형정석으로 입금해주시면 됩니다.',
        u'감사합니다!!'
    ]

    message_list[u'이상헌7538'] = [
        u'상헌아!',
        u'이렇게 결혼소식을 알리게 되서 미안하고',
        u'결혼식에 초대하지 못해서 또 미안하다 ^^;;',
        u'결혼 생활은 잘 하고 있는거지?',
        u'나도 그 대열에 이제 합류하려 한다! ㅎㅎ',
        u'이것저것 준비한다고 정신없는데 결혼 후에 한번 보자!',
    ]

    message_list[u'고은혜0821'] = [
        u'은혜누나',
        u'이렇게 결혼소식을 알리게 되서 죄송하고',
        u'결혼식에 초대하지 못해서 죄송해요 ^^;;',
        u'요즘도 여행 잘 다니고 교회 봉사 잘 하고 계신거죠? ㅎ',
        u'이것저것 준비한다고 정신없는데 결혼 후에 한번 얼굴 같이 뵈요!',
    ]

    message_list[u'권혜진0921'] = [
        u'혜진아',
        u'이렇게 결혼소식을 알리게 되서 미안해',
        u'남편이랑은 잘 지내고 결혼 생활은 어떤지 모르겠다 ㅎ',
        u'이것저것 준비한다고 정신없는데 결혼 후에 한번 얼굴 같이 보자!',
        u'결혼식과 결혼을 위해 기도 많이 해줘!',
    ]

    message_list[u'김슬아1115'] = [
        u'슬아야',
        u'이렇게 결혼소식을 알리게 되서 미안하다',
        u'결혼하고 난 후 남편이랑은 잘 지내고 있지? ㅎ',
        u'난 여전히 정신 없이 살고 결혼식도 벌여놓은게 많아서 수습하느라 바쁘다 ㅎ',
        u'결혼 후에 연락해서 한번 다같이 보자!',
        u'잘 지내고!',
    ]

    message_list[u'박소현3257'] = [
        u'소현아',
        u'이렇게 결혼소식을 알리게 되서 미안해',
        u'내가 벌려놓은 일이 많다보니 시간에 쫓기고 ㅎ',
        u'별다른 일 없이 잘 지내고 있는거지?',
        u'결혼 후에 연락해서 한번 다같이 보자!',
        u'잘 지내고~',
    ]

    message_list[u'박윤경2607'] = [
        u'윤경이 누나',
        u'몸도 아프신데도 불구하고',
        u'가교를 위해서 애쓰시고 본받을 모습이 많은거 같아요.',
        u'준상이와 준하, 남편분, 그리고 누나를 위해 더 기도할께요!',
        u'결혼식에 참석해주셔서 감사합니다!',
    ]

    message_list[u'정미영3364'] = [
        u'미영이 누나',
        u'바쁘게 삶을 꾸려가시는 모습도 좋지만',
        u'몸 건강도 항상 챙시기구요!',
        u'가교에서 자주 못뵙는게 아쉽고 얘기할 시간이 적어졌지만',
        u'종종 가끔 가교도 찾아오셔서 얘기하고 그래요~',
        u'결혼을 위해 기도 부탁드릴께요~',
    ]

    message_list[u'김종래2007'] = [
        u'종래야',
        u'결혼식에 초대하지 못해서 미안하고',
        u'이렇게 결혼을 알리게 되어서 미안하다 ㅎㅎ',
        u'내가 정신없이 일을 너무 크게 벌려서 ㅋㅋ',
        u'알지 무슨 마음인지? ㅋㅋ',
        u'결혼 후에 언제 배드민턴 한번 쳐야지?',
        u'나중에 또 보자!!',
    ]

    message_list[u'이재석7137'] = [
        u'재석아',
        u'결혼 생활은 잘 하고 있니?',
        u'이렇게 결혼을 알리게 되어서 미안하다 ㅎㅎ',
        u'정신없이 준비하다보니 어느새 시간이 이렇게 흘러버렸네',
        u'나도 이제 유부남 대열에 곧 들어간다!',
        u'나중에 얼굴 한번 볼 수 있으면 좋겠다~',
        u'Selalu menjaga kesehatanmu! tetap terhubungya!',
    ]

    message_list[u'이미선6599'] = [
        u'미선이 누나',
        u'요즘 잘 지내고 계셔요?',
        u'벌써 아이도 2명이나 되시고 ㅎㅎ',
        u'어머니 고수가 다 되셨겠네요 ^^;;',
        u'멀리서 가족끼리 한다고 초대는 못했지만',
        u'나중에 한번 얼굴 찾아뵈러 갈께요!',
        u'Selalu menjaga kesehatanmu! tetap terhubungya!',
    ]

    message_list[u'조일환2841'] = [
        u'일환아',
        u'결혼은 잘 했고 신혼여행은 어떠니? ㅎ',
        u'나도 너를 따라 곧 결혼을 한다 ㅎ',
        u'결혼식에 참석하지는 못하지만',
        u'멀리서나마 나의 결혼을 위해 기도 많이 부탁한다!',
        u'결혼 후에 한번 또 보자!'
    ]

    message_list[u'정찬송6242'] = [
        u'찬송아',
        u'잘 지내고 있니?',
        u'결혼 생활은 좋지? ㅎㅎ',
        u'나도 어서 그 생활에 동참하려고~',
        u'멀리서 가족끼리 한다고 초대는 못했지만',
        u'나중에 두석이랑 같이 얼굴 한번 볼 수 있으면 좋겠다.',
        u'생각날때마다 나를 위해서 기도 부탁해!',
        u'몸 건강히 잘 지내고~',
    ]

    message_list[u'강정훈2800'] = [
        u'정훈아',
        u'항상 열심히 활동하는 모습 페북을 통해 잘 보고 있어~',
        u'영캠때보다 더 멋진 사람이 되어가는거 같아서',
        u'그리고 함께 나누었던 그 얘기들을 차근차근 밟아나가고 있는거 같아서',
        u'혼자서 괜히 흐뭇해하고 있다 ㅎㅎ',
        u'서로의 영역에서 멋진 사람이 되었으면 좋겠다!',
        u'잘 지내고~ 기도 많이 부탁해',
    ]

    message_list[u'강진원5859'] = [
        u'진원아',
        u'잘 지내고 있니?',
        u'결혼 생활은 멋지게 잘 하고 있겠지?',
        u'나도 이제 유부남 대열에 들어가려고~',
        u'기도 많이 부탁한다~',
    ]

    message_list[u'강창모6041'] = [
        u'창모야',
        u'잘 지내고 있는지 모르겠다~',
        u'함께 고생시켰던 시간이 정말 멀지 않은거 같은데',
        u'벌써 3-4년이라는 시간이 훌쩍 지나가버렸네',
        u'결혼 생활은 알콩달콩 잘 하고 있지?',
        u'결혼을 위해 많은 기도 부탁한다~',
        u'나중에 애들 다같이 모여서 한번 보면 좋겠다~',
    ]

    message_list[u'고빈섭4597'] = [
        u'빈섭이형',
        u'최근에 결혼 축하드리구요~',
        u'저도 곧 그 대열에 합류합니다! ㅎㅎ',
        u'저에게 항상 멋진 프로그래머로 기억되고 계시는 빈섭옹!',
        u'결혼을 위해 기도 많이 부탁드려요~',
    ]

    message_list[u'고선우0623'] = [
        u'선우야',
        u'잘 지내고 있니?',
        u'페북을 가끔보니 잘 놀고 다니는거 같드라? ㅎㅎ',
        u'나는 곧 유부남 대열에 들어간다~',
        u'기도 많이 부탁하고~',
        u'진짜 얼굴 한번 보자 짜식아 ㅋㅋ',
    ]

    message_list[u'공수재5742'] = [
        u'수재수재형! ㅋ',
        u'잘 계시죠?',
        u'결혼 선배님께 저도 이제 곧 유부남 대열에 들어간다고 신고합니다 ㅎ',
        u'수재형이 항상 익살스럽게 장난치셨던게 항상 기억에 남아요 ㅎㅎ',
        u'결혼을 위해서 기도 많이 부탁드려요!',
    ]

    message_list[u'곽성훈8599'] = [
        u'성훈아',
        u'잘 지내고 있니?',
        u'글을 쓰려다 보니 4학년때 같이 스터디하던 때가 문득 떠오른다. ㅎㅎ',
        u'참 재미있었던거 같은데 ㅎ',
        u'벌써 시간이 흘러 결혼한다고 이렇게 알리게 되었네 ㅎ',
        u'기도 많이 부탁해!',
    ]

    message_list[u'김경식3663'] = [
        u'경식아',
        u'잘 지내고 있니?',
        u'열심히 프로그래머의 길을 걷고 있다고 소식을 들었던거 같은데',
        u'화이팅하고!! 난 이제 결혼을 해서 헛헛..',
        u'기도 많이 부탁한다!',
    ]

    message_list[u'김상헌5100'] = [
        u'상헌아',
        u'잘 지내고 있니?',
        u'바쁘게 보내다보니 배드민턴은 커녕 운동하기가 힘들구나 ㅎㅎ',
        u'결혼 하고 나면 좀 그런 시간을 가질수 있으려나.. ㅎㅎ',
        u'결혼 소식 이렇게 알리게 되서 미안하고',
        u'축하 메세지 하나 써줘 ~ ㅎㅎ',
    ]

    message_list[u'김선엽5275'] = [
        u'선엽아',
        u'이렇게 결혼소식을 알리게 되어 미안혀 ㅎ',
        u'가끔 페북보며 소식은 알고 있지만',
        u'연락자주 못해서 미안하고 ㅎ',
        u'결혼을 위해 기도 많이 부탁해!',
    ]

    message_list[u'김성훈9171'] = [
        u'성훈아',
        u'잘 지내고 있지?',
        u'항상 바르게(?) 생각하고 열심을 다하는 멋진 후배로 기억하고 있단다 ㅎ',
        u'결혼 소식을 이렇게 전해 미안하고',
        u'결혼을 위해 많은 기도 부탁할께!',
    ]

    message_list[u'김세현4318'] = [
        u'세현이형',
        u'코이카 선배님 ㅎㅎ',
        u'이제 제가 결혼합니다 ㅎㅎ',
        u'가족끼리 조촐하게 진행한다고 초대하지는 못했지만',
        u'결혼을 위해 많은 기도 부탁드릴께요.',
    ]

    message_list[u'김영성9670'] = [
        u'영성이형',
        u'예전에 형에게 청첩장 받고 밥 얻어먹었던 기억이 나는데',
        u'어느덧 제가 이렇게 결혼을 하게 되었습니다 ㅎㅎ',
        u'연락도 자주 못드렸는데 아쉽네요 ^^;;',
        u'결혼을 위해 기도 부탁드립니다!',
    ]

    message_list[u'김인중1415'] = [
        u'김인중 교수님 안녕하세요!',
        u'제가 드디어(?) 결혼합니다 ㅎ',
        u'이래저래 부족한 모습이지만 하나님의 은혜안에 좋은 짝을 만났어요~',
        u'결혼 전에 같이 찾아뵙고 인사드려야하는데 죄송합니다.',
        u'조만간 한번 찾아뵙도록 하겠습니다.',
        u'기도 많이 부탁드릴께요!',
    ]

    message_list[u'김장호4162'] = [
        u'장호야!',
        u'잘 지내고 있니? ㅎ',
        u'내가 이제서야 결혼을 하게 되었다 ㅋㅋ',
        u'라식 수술하고 더 멋져진 장호 ㅋ',
        u'결혼을 위해 기도 부탁한다!',
    ]

    message_list[u'김정인2595'] = [
        u'정인아',
        u'잘 지내고 있지?',
        u'내가 드디어 결혼을 하게 되어 이렇게 청첩장을 보냈어!',
        u'그때 정인이의 센스로 받은 넥타이는 잘 쓰고 있다~',
        u'항상 힘내고 결혼을 위해 기도 부탁한다!',
    ]

    message_list[u'김종규0912'] = [
        u'종규형',
        u'잘 지내고 계시죠?',
        u'제가 드디어 결혼합니다 ㅎㅎ',
        u'멀리서나마 기도로 축복해주세요~',
        u'항상 신경써주셔서 감사했습니다!',
    ]

    message_list[u'김현숙7986'] = [
        u'현숙아',
        u'잘 지내고 있지?',
        u'내가 드디어 결혼한다 헛헛',
        u'멀리서나마 기도해주고~ 축복해주렴!',
        u'몸 건강하고 화이팅!',
    ]

    message_list[u'김형규9581'] = [
        u'형규형',
        u'잘 지내고 계신가요?',
        u'제가 드디어 결혼합니다 ㅎ',
        u'기도 많이 부탁드려요~',
    ]

    message_list[u'김호진4212'] = [
        u'호진 간사님!',
        u'ㅠ_ㅠ 왠지 죄송한 마음이 많이 듭니다.',
        u'결혼한다고 너무 도와드리지 못해서 죄송하구요',
        u'언능 바쁨을 정리하고 복귀하겠습니다!',
        u'결혼을 위해 기도 부탁드릴께요!',
    ]

    message_list[u'명지윤9445'] = [
        u'지윤아',
        u'잘 지내고 있니? ㅎ',
        u'여전히 명랑하고 씩씩(?)하게 잘 지내고 있겠지? ㅋ',
        u'내가 드디어 결혼하게 되어.. 이렇게 청첩장을 만들었어 ㅎㅎ',
        u'항상 잘 지내고 기도 부탁할께!',
    ]

    message_list[u'박구원9019'] = [
        u'구원아',
        u'잘 지내고 있지?',
        u'내가 결국 결혼하게 되어서! ㅋ',
        u'이렇게 결혼을 알리게 되었어',
        u'많이 기도 해줘~',
    ]

    message_list[u'박상용3256'] = [
        u'상용이형',
        u'잘 지내고 계시죠?',
        u'제가 드디어 결혼을 합니다 ㅎ',
        u'많은 기도 부탁드릴께요~',
    ]

    message_list[u'박상준0834'] = [
        u'상준님? ㅎㅎ',
        u'아직 어색하지만 혹시나 들어올까봐',
        u'메세지 남겨놓습니다~',
        u'저도 이제 결혼하게 되었네요~',
        u'기도 후원 부탁드릴께요~',
    ]

    message_list[u'박신혜3450'] = [
        u'신혜야',
        u'잘지내고 있니? ㅋ',
        u'나도 결혼한다 ㅎ',
        u'많이 기도해주라~ ㅎ',
    ]

    message_list[u'박신홍0409'] = [
        u'신홍아',
        u'잘 지내고 있지?',
        u'어느덧 나이를 먹어 나도 결혼을 하게 되었구먼 ㅎㅎ',
        u'신홍이도 좋은 짝 어서 만나기를 ㅎㅎ',
        u'기도 많이 해주라~',
    ]

    message_list[u'박아론0819'] = [
        u'아론아',
        u'잘 지내고 있니? ㅎ',
        u'나도 어느덧 나이를 먹고 결혼을 하게 되었어! ㅎ',
        u'많이 기도해주고 응원부탁해 ㅎ',
    ]

    message_list[u'박주로2997'] = [
        u'주로야',
        u'잘 지내고 있지?',
        u'여전히 바쁘게 지내고 있으리라 생각한다 ㅎ',
        u'나도 이제 결혼이란 문에 들어가게 되었구먼 ㅎ',
        u'많이 기도해주고~ 잘지내!',
        u'결혼식에 초대하지 못해서 미안해~',
    ]

    message_list[u'박지환1870'] = [
        u'지환아',
        u'잘 지내고 있지? ㅎ',
        u'어때 결혼생활은? ㅎㅎ',
        u'나도 이제 결혼을 하게 되어 이렇게 메세지를 남겨!',
        u'많이 기도해주길! ㅎ',
    ]

    message_list[u'박진선7004'] = [
        u'진선이 누나',
        u'잘 계시는거죠? ㅎ',
        u'저도 이제 결혼을 하게 되었습니다 ㅎㅎ',
        u'기도 많이 해주세요! : )',
    ]

    message_list[u'박한나6034'] = [
        u'한나야',
        u'잘 지내고 있지?',
        u'혹시나 볼까 싶어 이렇게 메세지를 남긴다.',
        u'나도 이제 결혼을 하게 되어서 ㅎ',
        u'기도 많이 해주고~ 항상 몸 잘 챙기고!',
    ]

    message_list[u'박한별9991'] = [
        u'한별이형!',
        u'잘 지내고 계시죠? ㅎ',
        u'저도 이제 결혼합니다!!',
        u'준비한다고 정신없어서 이제서야 알려서 죄송하구요~',
        u'기도 많이 해주세요!! : )',
    ]

    message_list[u'배은정7751'] = [
        u'은정아',
        u'잘 지내고 있지?',
        u'나도 이제 결혼을 하게 되어 이렇게 메세지를 남겨',
        u'생각날때 기도 해주고~ 네가 하는일도 잘 되길 응원한다!',
    ]

    message_list[u'백현욱8524'] = [
        u'현욱아',
        u'이 메세지를 보게될 확률은 적지만',
        u'혹시나 하는 마음에 남긴다~',
        u'나도 이제 결혼을 하게 되었어!',
        u'멀리서 기도로 응원해주면 좋을거 같아!',
        u'너도 화이팅하고! ^^',
    ]

    message_list[u'손착한5516'] = [
        u'착한아',
        u'잘 지내고 있지?',
        u'내가 이제 결혼하게 되어 이렇게 메세지를 남겨',
        u'배드민턴 요즘도 열심히 치고 있나? ㅎㅎ',
        u'나도 결혼하고 배드민턴 다시 시작하고 싶다 ㅎㅎ',
        u'항상 힘내고 멀리서나마 시간날때 기도해줘~',
    ]

    message_list[u'손혜영1406'] = [
        u'혜영이 누나',
        u'잘 지내고 계시죠?',
        u'이렇게 결혼소식을 알리게 되어 죄송해요 ㅎㅎ',
        u'항상 몸 잘챙기시고~',
        u'생각날때 결혼을 위해 기도 부탁드릴께요~',
    ]

    message_list[u'신기준5778'] = [
        u'기준아',
        u'잘 지내고 있지?',
        u'어느덧 나도 결혼이란걸 하게 되었구나 ㅎㅎ',
        u'결혼 선배인 너는 아이 낳고 정신없지 잘 지내고 있으리라 생각해~ ㅎ',
        u'멀리서나마 기도해주고! 화이팅이다~',
    ]

    message_list[u'신성현4907'] = [
        u'성현이형',
        u'잘 지내고 계시죠?',
        u'어느덧 저도 결혼할 때가 되었어요 ㅎ',
        u'간간히 양육 블로그 글은 잘 보고 있습니다 ㅎㅎ',
        u'결혼을 위해 멀리서나마 기도해주시고 응원해주세요!',
    ]

    message_list[u'양신용8850'] = [
        u'신용아',
        u'잘 지내고 있니?',
        u'혹시나 하는 마음에 이렇게 메세지를 남긴다!',
        u'항상 몸 건강히 잘 지내고!',
        u'결혼을 위해 기도해주고 응원해줘!',
    ]

    message_list[u'양현주2266'] = [
        u'현주야',
        u'잘 지내고 있지?',
        u'나도 어느덧 결혼이란걸 하게 되어서 ㅎㅎ',
        u'결혼을 위해 기도해주고 응원해줘!',
    ]

    message_list[u'오규범5269'] = [
        u'규범아',
        u'잘 지내고 있지?',
        u'어느덧 내가 결혼이란걸 하게되어서 ㅎㅎ',
        u'소식은 잘 못듣고 있지만 항상 건강하고!',
        u'결혼을 위해 기도해주고 응원해줘!',
    ]

    message_list[u'원현희8996'] = [
        u'현희야',
        u'잘 지내고 있지? ㅎ',
        u'이 메세지를 볼지는 모르겠다만 ㅎ',
        u'나도 어느덧 너를 따라(?) 결혼을 하게 되었구나 ㅎ',
        u'결혼을 위해 기도해주고 응원해줘~',
    ]

    message_list[u'유원대9007'] = [
        u'원대형',
        u'혹시나 하는 마음에 메세지 남겨놔요 ㅎㅎ',
        u'저도 이제 결혼을 합니다 ㅎㅎ',
        u'생각날때 결혼을 위해 기도해주시고 응원해주세요!',
    ]

    message_list[u'이강0804'] = [
        u'이강교수님 안녕하세요!',
        u'이렇게 결혼소식을 알려드려 죄송합니다.',
        u'많은 일들을 벌여놓다보니 챙기지 못한 부분이 많아서 죄송하네요.',
        u'한번 뵈러 가야하는데 마음만 먹다가 계속 못하고 있네요..',
        u'멀리서나마 기도해주시고 응원해주세요.',
        u'조만간 연락드리겠습니다!',
    ]

    message_list[u'이만성3801'] = [
        u'이만성 장로님!',
        u'혹시나 번호가 맞으면 이 메세지를 보시겠지요?',
        u'인도네시아에서 정말 많은 도움을 주신것',
        u'잊지 않고 기억하고 있습니다!',
        u'제가 이렇게 많은 분들의 사랑의 손길을 받아',
        u'좋은 배우자를 만나 결혼까지 하게 되었어요',
        u'결혼을 위해 기도해주시고 응원해주세요~',
    ]

    message_list[u'이선화5606'] = [
        u'선화야',
        u'잘 지내고 있지?',
        u'나도 이제 결혼을 하게되어 이렇게 메세지를 남긴다~',
        u'생각날때 결혼을 위해 기도해주고 응원부탁할께!',
    ]

    message_list[u'이수진9356'] = [
        u'수진이 누나!',
        u'잘 지내고 있죠? 결혼생활도 잘하고 계시고? ^^;;',
        u'저도 이제 결혼을 하게 되어 이렇게 메세지 남겨요~',
        u'생각날때 결혼을 위해 기도해주시고 응원 부탁할께요~',
    ]

    message_list[u'이승민5832'] = [
        u'승민아',
        u'잘 지내고 있지?',
        u'항상 열정을 가진 너의 페북 활동을 잘 지켜보고 있어! ㅎㅎ',
        u'나도 이제 결혼을 하게되어 이렇게 메시지를 남긴다~',
        u'결혼을 위해 기도해주고 응원부탁할께~',
    ]

    message_list[u'이승주3414'] = [
        u'승주야',
        u'잘 지내고 있지?',
        u'아이 낳고 정신없을거 같다 ㅎㅎ',
        u'나도 이제 결혼을 하게 되어 이렇게 메세지를 남겨~',
        u'생각날때 기도해주고 응원해주길!',
    ]

    message_list[u'이예은3940'] = [
        u'예은아',
        u'잘 지내고 있지?',
        u'나도 이제 결혼을 하게되어 이렇게 메세지를 남겨',
        u'생각날때 기도해주고 응원해주길 바랄께 ㅎ',
    ]

    message_list[u'이진아3332'] = [
        u'진아누나',
        u'잘 지내고 계신거죠? ㅎㅎ',
        u'혹시나 메세지 볼까바 이렇게 글 남겨요~',
        u'저도 이제 결혼을 하게되었네요 ㅎㅎ',
        u'참 시간 빠른거 같아요 ㅎㅎ',
        u'생각나실때 결혼을 위해 기도해주시고 응원해주세요~',
    ]

    message_list[u'임새미5241'] = [
        u'새미야',
        u'잘 지내고 있니?',
        u'나도 이제 결혼을 하게되어 이렇게 메세지를 남긴다~',
        u'생각날때 결혼을 위해 기도해주고 응원부탁할께~',
    ]

    message_list[u'장경록9622'] = [
        u'경록아',
        u'잘 지내고 있지?',
        u'여전히 공부 열심히 하고 멋진 모습으로 있을거 같다 ㅎㅎ',
        u'나도 이제 결혼을 하게되어 이렇게 메세지를 남겨~',
        u'생각날때 결혼을 위해 기도해주고 응원부탁할께~',
    ]

    message_list[u'장영두9207'] = [
        u'영두형!',
        u'잘 지내고 계시죠?',
        u'저도 이제 결혼을 하게 되었어요',
        u'시간이 어느덧 이렇게 흘러가버렸네요ㅎㅎ',
        u'앞으로 결혼생활도 잘 할수 있도록 기도부탁할께요~',
    ]

    message_list[u'장효중0815'] = [
        u'효중아~',
        u'잘 지내고 있지?',
        u'내가 기억하는 효중이는 참 멋있는 사람인데 말이여 ㅎㅎ',
        u'여전히 멋있겠지? ㅋㅋ',
        u'어느덧 시간이 흘러 나도 결혼을 하게 되어 이렇게 메세지를 남긴다~',
        u'생각날때 기도해주고 응원해줘~',
    ]

    message_list[u'전승규0413'] = [
        u'승규찡?',
        u'잘 지내고 있어? ㅎㅎ',
        u'시간이 너무 빨리 흘러서 나도 결혼을 하게 되었어 ㅋ',
        u'이렇게 소식을 전하게 되어 미안하고~',
        u'결혼을 위해 기도해주고 응원 부탁할께~',
    ]

    message_list[u'정다희8529'] = [
        u'다희누나',
        u'잘 계시죠?',
        u'어느정 저도 결혼이란걸 하게 되어 혹시나 하는 마음에 메세지를 남겨요',
        u'생각날때 기도해주시고 응원해주세요~',
    ]

    message_list[u'정제니9921'] = [
        u'제니누나',
        u'잘 지내고 계시죠?',
        u'결혼 생활은 좋으신가요 ^^;;',
        u'저도 이제 결혼을 하게되어 이렇게 소식을 전해요~',
        u'생각날때 기도해주시고 응원해주세요~',
    ]

    message_list[u'정중은1147'] = [
        u'중은아 예~',
        u'잘 지내고 있지? ㅎㅎ',
        u'나도 이제 결혼을 하게 되어 이렇게 소식을 전한다~',
        u'항상 열심히 노력하는 중은이니까 어디서든 잘하고 있으리라 생각한다!',
        u'생각날때 결혼을 위해 기도해주고 응원부탁할께~',
    ]

    message_list[u'정진희9525'] = [
        u'진희야',
        u'잘 지내고 있지?',
        u'어느덧 시간이 흘러 나도 결혼을 하게 되었어~',
        u'생각날때 기도해주고 응원부탁할께~',
    ]

    message_list[u'정하영1107'] = [
        u'하영아!',
        u'잘 지내고 있지?',
        u'내가 드디어 결혼을 하게 되었다 ㅎㅎ',
        u'참 시간이 빨리 지나가는거 같어..',
        u'너도 곧 좋은 배우자 만나서 좋은 소식 전해주고!',
        u'생각날때 기도해주고 응원부탁할께~',
    ]

    message_list[u'조영석9419'] = [
        u'영석이형 안녕하세요~',
        u'잘 지내고 계시죠? ㅎ',
        u'저도 어느덧 시간이 흘러 결혼을 하게 되었네요 ㅎ',
        u'결혼을 위해 기도해주시고 응원부탁할께요~',
    ]

    message_list[u'조현민8341'] = [
        u'현민이형',
        u'잘 계시죠? ㅎ',
        u'페북을 통해 간간히 소식을 보고 있어요~',
        u'멋진 감독이 되시길 응원할께요~',
        u'저도 어느덧 시간이 흘러 결혼을 하게 되어 이렇게 메세지 남겨요~',
        u'생각나실 때 기도해주시고 응원부탁드려요~',
    ]

    message_list[u'조혜근2731'] = [
        u'혜근이형',
        u'잘 지내고 계시죠? ㅎㅎ',
        u'결혼 생활은 달달하신가요? ㅋㄷ',
        u'저도 결혼을 하게 되어 이렇게 메세지 남깁니다 ㅎㅎ',
        u'생각나실 때 기도해주시고 응원부탁드려요~ ㅎ',
    ]

    message_list[u'지승영8144'] = [
        u'승영아',
        u'잘 지내고 있지? ㅎㅎ',
        u'삼성맨으로서 잘 성장하고 있는지 궁금하기도 하네 ㅎ',
        u'나도 결혼을 하게 되어 이렇게 메시지를 남긴다~',
        u'생각날 때 기도해주고 응원 부탁할께~',
    ]

    message_list[u'차진호5800'] = [
        u'차진호 목사님',
        u'잘 지내고 계시죠? ^^',
        u'작은 예수를 얘기하셨던 그때의 그 모습을 아직도 선명하게 기억합니다~',
        u'저도 이제 결혼을 하게되어 이렇게 소식을 전해요~',
        u'생각나실 때 기도해주시고 응원부탁드릴께요~',
    ]

    message_list[u'채미현7196'] = [
        u'미현아',
        u'잘 지내고 있지? ㅎ',
        u'요즘은 뭘 하며 지내고 있는지 궁금하구먼 ㅎ',
        u'나도 결국 결혼을 하게되어 이렇게 소식을 전해~',
        u'생각날때 기도해주고 응원 부탁할께~',
    ]

    message_list[u'채송화9760'] = [
        u'송화야',
        u'잘 지내고 있지?',
        u'결혼 생활은 어찌 달달한고? ㅎ',
        u'나도 결혼을 하게되어 이렇게 소식을 전한다~',
        u'생각날 때 기도해주고 응원 부탁할께~',
    ]

    message_list[u'최건희2997'] = [
        u'건희님(?) ㅎㅎ',
        u'아직도 이 어색한 호칭을 버리기 힘들군요 ㅎㅎ',
        u'그때도 말씀드렸듯이 저도 이제 결혼합니다!',
        u'저번에 장소 잘 빌려주셔서 감사드리구요~',
        u'생각날때 기도해주시고 응원 부탁드려요!',
    ]

    message_list[u'최나랑7464'] = [
        u'나랑이 누나',
        u'잘 지내고 계시죠?',
        u'공부는 할만하셔요? ㅎㅎ',
        u'저도 이제 결혼을 하게되어 이렇게 소식 전해드려요~',
        u'생각나실때 기도해주시고 응원 부탁드려요~',
    ]

    message_list[u'최미나4821'] = [
        u'미나누나',
        u'잘 지내고 계시죠? ㅎ',
        u'저도 이제 결혼을 하게되어 이렇게 소식 전해요~',
        u'생각나실 때 기도해주시고 응원 부탁드릴께요~',
    ]

    message_list[u'최성민4580'] = [
        u'성민이형',
        u'잘 계시죠?',
        u'요즘 얼굴을 못뵌거 같아서 궁금했어요 ㅎㅎ',
        u'저도 이제 결혼을 하게되어 이렇게 소식을 전해요~',
        u'생각나실 때 기도해주시고 응원 부탁드릴께요~',
    ]

    message_list[u'최성원7009'] = [
        u'성원아',
        u'잘 지내고 있지? ㅎ',
        u'수염은 잘 깍고 다니는지 모르겠다 ㅋㅋ',
        u'나도 결혼을 해서 이렇게 소식을 전한다~',
        u'생각날때 기도 해주고 응원 부탁할께~',
    ]

    message_list[u'최인석6280'] = [
        u'인석아',
        u'잘 지내고 있지?',
        u'나도 결혼을 하게 되어 이렇게 소식을 전해~',
        u'생각날 때 기도해주고 응원 부탁할께~',
    ]

    message_list[u'추경식9760'] = [
        u'경식이형 ㅋ',
        u'잘 계시죠? ㅎㅎ',
        u'항상 경식이형만 보면 맞을까바 두려움에 떨었던 날들이 생각나네요 ㅋㅋ',
        u'저도 이제 결혼을 하게되어 이렇게 소식을 전해요',
        u'생각날 때 기도해주시고 응원 부탁할께요~',
    ]

    message_list[u'추신우3791'] = [
        u'신우형',
        u'최근에 좋은 이야기도 많이 해주시고 시간내주셔서 감사합니다~',
        u'앞으로 제가 더욱 더 성장하게 되길 기대해봅니다 ㅎㅎ',
        u'이렇게 결혼소식을 전하게 되어 죄송하고',
        u'생각나실때 기도로 후원 부탁드릴께요~!',
    ]

    message_list[u'하동우3296'] = [
        u'동우야',
        u'잘 지내고 있지? ㅎ',
        u'결혼 생활은 어찌 달달하게 잘 보내고 있니? ㅎ',
        u'나도 이제 결혼을 하게되어 이렇게 소식을 알린다~',
        u'생각날 때 기도해주고 응원부탁할께~',
    ]

    message_list[u'한서령0313'] = [
        u'서령아',
        u'잘 지내고 있지? ㅎㅎ',
        u'번호가 있어서 혹시나 하는 마음에 메세지를 남겨~',
        u'시간이 흘러 나도 이제 결혼을 한다고 알리는 시간이 왔네 ㅎㅎ',
        u'생각날때 기도해주고 응원부탁할께~',
    ]

    message_list[u'허지행9234'] = [
        u'지행아',
        u'잘 지내고 있지?',
        u'예전에 한번 얼굴본다고 하다가 결국 못보고 지금까지 왔네 ㅎㅎ',
        u'참 시간 내는게 어려운 세상이라니 @_@',
        u'나도 이제 결혼을 해서 이렇게나마 소식을 전한다~',
        u'생각날 때 기도해주고 응원부탁할께~',
    ]

    message_list[u'황병일0631'] = [
        u'병일아',
        u'잘 지내고 있지?',
        u'난 네가 항상 자신감있게 살고 밝았으면 좋겠다!',
        u'너는 그런 모습이 멋지거든 ㅋㅋ',
        u'나도 이게 결혼을 하게 되었다니 참 ㅎㅎ 실감안나는군',
        u'생각날때 기도해주고 응원부탁할께~',
    ]

    message_list[u'황정한2346'] = [
        u'정한아',
        u'잘 지내고 있니?',
        u'시인같았던 네가 요즘은 뭘 하고 있는지 궁금하기도 하고 ㅎㅎ',
        u'나도 이제 결혼을 하게되어 이렇게 메세지를 남긴다~',
        u'생각날때 기도해주고 응원부탁할께~',
    ]

    for _to, _messages in message_list.iteritems():
        default_message_add(default_user, _to, _messages)


def default_message_add(_from, _to, messages):

    for message in messages:
        default_message = DefaultMessages()
        default_message.target = _to
        default_message.message = message
        default_message.user = _from
        default_message.created_at = timezone.now()
        default_message.save()


def register_invited_persons():

    invited_list = [
        {'name': u'방준성'},
        {'name': u'차효준'},
        {'name': u'정나래'},
        {'name': u'김효현'},
        {'name': u'신영섭'},
        {'name': u'이광영'},
        {'name': u'이찬규'},
        {'name': u'김지훈'},
        {'name': u'허두석'},
        {'name': u'권오현'},
        {'name': u'김다슬'},
        {'name': u'조일희'},
        {'name': u'정성진'},
        {'name': u'정희원'},
        {'name': u'이건희'},
        {'name': u'강인구'},
        {'name': u'박윤경'},
        {'name': u'전상호'},
        {'name': u'서준석'},
        {'name': u'박경찬'},
        {'name': u'김준형'},
        {'name': u'이루리'},
        {'name': u'김자연'},
        {'name': u'김가영'},
        {'name': u'변지영'},
        {'name': u'길종훈'},
        {'name': u'박영훈'},
        {'name': u'김재익'},
        {'name': u'정은미'},
        {'name': u'서재오'},
        {'name': u'윤상웅'},
        {'name': u'안혜진'},

        {'name': u'손선화'},
        {'name': u'손선미'},
        {'name': u'이혜민'},
        {'name': u'박우정'},
        {'name': u'김생화'},
        {'name': u'김혜지'},
        {'name': u'박희연'},
        {'name': u'구자민'},
        {'name': u'장성은'},
        {'name': u'문슬기'},
        {'name': u'노서영'},
        {'name': u'송하나'},
        {'name': u'윤세진'},
        {'name': u'이은경', 'last_number': 9063},
        {'name': u'남수해'},
        {'name': u'황성혜'},
        {'name': u'김슬아'},
        {'name': u'윤보연'},
        {'name': u'김은진'},
        {'name': u'백성훈'},
        {'name': u'김재윤'},
        {'name': u'조호연'},
        {'name': u'이지섭'},
        {'name': u'김현정'},
        {'name': u'정승연'},
        {'name': u'김자경'},

        {'name': u'장원석'},
        {'name': u'김윤미'},
        {'name': u'임진경'},
        {'name': u'형성안'},
        {'name': u'김보선'},
        {'name': u'형우식'},
        {'name': u'형성길'},
        {'name': u'최갑남'},
        {'name': u'형승희'},
        {'name': u'형성래'},
        {'name': u'최점덕'},
        {'name': u'형지선'},
        {'name': u'신옥자'},
        {'name': u'김주영'},
        {'name': u'김춘희'},
        {'name': u'신현수'},
        {'name': u'김현식'},
        {'name': u'류승희'},
        {'name': u'신광수'},
        {'name': u'류정희'},
        {'name': u'김기호'},
        {'name': u'류남순'},
        {'name': u'양경욱'},
        {'name': u'류휘경'},
        {'name': u'권인숙'},
        {'name': u'류기성'},
        {'name': u'류희문'},
        {'name': u'윤미나'},
        {'name': u'양용규'},
        {'name': u'신옥순'},
        {'name': u'형성욱'},
        {'name': u'류희순'},
        {'name': u'형지현'},

        {'name': u'백인애'},
        {'name': u'한달원'},
        {'name': u'김기남'},
        {'name': u'한승곤'},
        {'name': u'노나래'},
        {'name': u'한지연'},
        {'name': u'신현태'},
        {'name': u'한규원'},
        {'name': u'서형애'},
        {'name': u'한지윤'},
        {'name': u'김재은'},
        {'name': u'한지원'},
        {'name': u'이규화'},
        {'name': u'한승화'},
        {'name': u'신미남'},
        {'name': u'송홍근'},
        {'name': u'송지희'},
        {'name': u'송연태'},
        {'name': u'송선화'},
        {'name': u'유재구'},
        {'name': u'신중경'},
        {'name': u'김남욱'},
        {'name': u'신중한'},
        {'name': u'오현숙'},
        {'name': u'신범규'},
        {'name': u'신희라'},
        {'name': u'신중구'},
        {'name': u'박명숙'},
        {'name': u'신헌규'},
        {'name': u'설은주'},
        {'name': u'최수혜'},
        {'name': u'한미령'},
        {'name': u'김진회'},
        {'name': u'이은경'},
        {'name': u'김명순'},
        {'name': u'도현석'},
        {'name': u'진명규'},
        {'name': u'유명희'},
        {'name': u'이두성'},
        {'name': u'박순례'},
        {'name': u'한철원'},
        {'name': u'신미현'},
  ]

    for person in invited_list:
        user = User()
        user.name = person['name']
        if 'last_number' in person:
            user.last_number = person['last_number']
        user.is_invited = True
        user.save()


def default_message_init():
    default_user = User.objects.get(name=u'한의주♥형정석', last_number=u'0104')

    messages = [
        u'안녕하세요. 한의주&형정석의 모바일 청첩장입니다.',
        u'오른쪽 상단 메뉴를 이용하시면 결혼식 정보 및 사진을 볼수 있어요!',
        u'저희에게 축복의 메세지를 여기에 남겨주시면 저희가 보고 답장드려요!'
    ]

    for message in messages:
        default_message = DefaultMessages()
        default_message.message = message
        default_message.user = default_user
        default_message.created_at = timezone.now()
        default_message.save()


def default_user_init():

    User(name=u'형정석', last_number=u'2857', is_staff=True, profile=u'hjs.png').save()
    User(name=u'한의주', last_number=u'9911', is_staff=True, profile=u'hej.png').save()
    User(name=u'한의주♥형정석', last_number=u'0104', is_staff=True, profile=u'hej_hjs.png').save()


def init_db(self, method_name):
    if not is_execute(method_name):
        eval(method_name + "()")
        execute_done(method_name)
        self.stdout.write('Execute %s db init OK' % method_name)


def execute_done(query_id):

    try:
        log = InitDatabaseLog.objects.get(query_id=query_id)
        log.is_execute = True
    except InitDatabaseLog.DoesNotExist:
        log = InitDatabaseLog()
        log.query_id = query_id
        log.is_execute = True

    log.save()


def is_execute(query_id):
    try:
        init_log = InitDatabaseLog.objects.get(query_id=query_id)
        return init_log.is_execute
    except InitDatabaseLog.DoesNotExist:
        return False
