function _ajax (option, method) {
  if (!option.dataType) {
    option.dataType = 'json'
  }
  $.ajax({
    url: option.url,
    method: option.method,
    data: option.data,
    success: function () {
      alert('success')
    },
    fail: function () {
      alert('fail')
    }
  })
};

export default {
  _ajax
}
