let isKakaoInitialized = false;

// Kakao SDK 초기화 함수
function initKakao(key) {
    if (!Kakao.isInitialized()) {
        Kakao.init(key);
        isKakaoInitialized = true;
        console.log("Kakao Initialized:", Kakao.isInitialized());
    }
}

// 템플릿 메시지 전송 함수
function sendKakaoTemplateMessage(templateId,title, description, path) {
    // 카카오 SDK 초기화 (키는 실제 키로 대체)
    initKakao('e9c5767d8ee779e382f134c8b69abf1d');

    if (!isKakaoInitialized) {
        console.error("Kakao SDK가 초기화되지 않았습니다.");
        return;
    }

    Kakao.Share.sendCustom({
      templateId: templateId,
      templateArgs: {
        title: title,
        description: description,
        path : path

      },
    });
}


