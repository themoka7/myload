 // 모달을 생성하고 표시하는 함수
        function showLoadingModal() {
            const modalHtml = `
                <div class="modal fade" id="loadingModal" tabindex="-1" role="dialog" aria-labelledby="loadingModalLabel" aria-hidden="true">
                    <div class="modal-dialog modal-dialog-centered" role="document">
                        <div class="modal-content modal-main">
                            <div class="modal-body text-center">
                                <!-- 원형 로딩바 -->
                                <div class="circle-container">
                                    <div class="circle">
                                        <div class="gua" style="transform: rotate(0deg) translate(80px);">乾</div>
                                        <div class="gua" style="transform: rotate(45deg) translate(80px);">坤</div>
                                        <div class="gua" style="transform: rotate(90deg) translate(80px);">震</div>
                                        <div class="gua" style="transform: rotate(135deg) translate(80px);">巽</div>
                                        <div class="gua" style="transform: rotate(180deg) translate(80px);">坎</div>
                                        <div class="gua" style="transform: rotate(225deg) translate(80px);">離</div>
                                        <div class="gua" style="transform: rotate(270deg) translate(80px);">艮</div>
                                        <div class="gua" style="transform: rotate(315deg) translate(80px);">兌</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            `;

            // 모달 HTML을 삽입
            document.getElementById('commonModalContainer').innerHTML = modalHtml;

            // 모달 열기
            $('#loadingModal').modal({
                backdrop: 'static', // 배경 클릭으로 닫히지 않게 설정
                keyboard: false     // ESC로 닫히지 않게 설정
            });


        }

        // 모달을 닫는 함수
        function closeLoadingModal() {
            $('#loadingModal').modal('hide');
        }

// 모달을 닫는 함수
function closeLoadingModal() {
    // 모달 닫기
    $('#loadingModal').modal('hide');

    // 모달이 닫히면 모달 HTML을 지워 메모리 절약
    $('#loadingModal').on('hidden.bs.modal', function () {
        document.getElementById('commonModalContainer').innerHTML = '';
    });
}
