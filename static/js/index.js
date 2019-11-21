document.addEventListener("keydown",keydown);
				//键盘监听，注意：在非ie浏览器和非ie内核的浏览器
				//参数1：表示事件，keydown:键盘向下按；参数2：表示要触发的事件
				function keydown(event){
					//表示键盘监听所触发的事件，同时传递参数event
					switch(event.keyCode){
						case 37:
						case 65:
							// console.log('左键');
							getXhrP_left();
							break;
						case 38:
						case 87:
							// console.log('上键');
							getXhrP_up();
							break;
						case 39:
						case 68:
							// console.log('右键');
							getXhrP_right();
							break;
						case 40:
						case 83:
							// console.log('下键');
							getXhrP_down();
							break;
					}
				};

function getXhrP_up(){
				//1.创建xhr
				var xhr = createXhr();
				//2.创建请求
				var url = '/ht2048/on/?on=up';
				xhr.open('get',url,true);
				//3.设置回调
				xhr.onreadystatechange = function(){
					if(xhr.readyState == 4 && xhr.status == 200){
						//获取array字符串
						var arr = xhr.responseText;
						//字符串转换json对象
						var arr = JSON.parse(arr).val;
						console.log(arr)
						if(arr == '没有变化'){
							console.log('没有变化')
						}else if(arr[arr.length-1]=='over'){
							arr.pop();
							plusmapover(arr);
							console.log('游戏结束')
							$(function (){
								setTimeout("over()",100); //延迟1秒
							})
						}else{
							Setcookie('arr',arr);
							plusmap(arr);
							console.log('上键');
						}

					}
				}
				//4.发送请求
				xhr.send(null);
			};

function Setcookie (name, value){
				//设置名称为name,值为value的Cookie
				var expdate = new Date();   //初始化时间
				expdate.setTime(expdate.getTime() + 30 * 60 * 1000);   //时间单位毫秒
				document.cookie = name+"="+value+";expires="+expdate.toGMTString()+";path=/";
			};

			function new_cookie (){
				//设置名称为name,值为value的Cookie
				var expdate = new Date();   //初始化时间
				var x1 = document.getElementById('x1').innerText;
				var x2 = document.getElementById('x2').innerText;
				var x3 = document.getElementById('x3').innerText;
				var x4 = document.getElementById('x4').innerText;
				var x5 = document.getElementById('x5').innerText;
				var x6 = document.getElementById('x6').innerText;
				var x7 = document.getElementById('x7').innerText;
				var x8 = document.getElementById('x8').innerText;
				var x9 = document.getElementById('x9').innerText;
				var x10 = document.getElementById('x10').innerText;
				var x11 = document.getElementById('x11').innerText;
				var x12 = document.getElementById('x12').innerText;
				var x13 = document.getElementById('x13').innerText;
				var x14 = document.getElementById('x14').innerText;
				var x15 = document.getElementById('x15').innerText;
				var x16 = document.getElementById('x16').innerText;
				value = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16]
				expdate.setTime(expdate.getTime() + 30 * 60 * 1000);   //时间单位毫秒
				document.cookie = "arr="+value+";expires="+expdate.toGMTString()+";path=/";
			};

			function getXhrP_down(){
				//1.创建xhr
				var xhr = createXhr();
				//2.创建请求
				var url = '/ht2048/on/?on=down';
				xhr.open('get',url,true);
				//3.设置回调
				xhr.onreadystatechange = function(){
					if(xhr.readyState == 4 && xhr.status == 200){
						//获取array字符串
						var arr = xhr.responseText;
						//字符串转换json对象
						var arr = JSON.parse(arr).val;
						console.log(arr)
						if(arr == '没有变化'){
							console.log('没有变化')
						}else if(arr[arr.length-1]=='over'){
							arr.pop();
							plusmapover(arr);
							console.log('游戏结束')
							$(function (){
								setTimeout("over()",100); //延迟1秒
							})
						}else{
							Setcookie('arr',arr);
							plusmap(arr);
							console.log('下键');
						}
					}
				}
				//4.发送请求
				xhr.send(null);
			};

			function getXhrP_left(){
				//1.创建xhr
				var xhr = createXhr();
				//2.创建请求
				var url = '/ht2048/on/?on=left';
				xhr.open('get',url,true);
				//3.设置回调
				xhr.onreadystatechange = function(){
					if(xhr.readyState == 4 && xhr.status == 200){
						//获取array字符串
						var arr = xhr.responseText;
						//字符串转换json对象
						var arr = JSON.parse(arr).val;
						console.log(arr)
						if(arr == '没有变化'){
							console.log('没有变化')
						}else if(arr[arr.length-1]=='over'){
							arr.pop();
							plusmapover(arr);
							console.log('游戏结束')
							$(function (){
								setTimeout("over()",100); //延迟1秒
							})
						}else{
							Setcookie('arr',arr);
							plusmap(arr);
							console.log('左键');
						}
					}
				}
				//4.发送请求
				xhr.send(null);
			};

			function getXhrP_right(){
				//1.创建xhr
				var xhr = createXhr();
				//2.创建请求
				var url = '/ht2048/on/?on=right';
				xhr.open('get',url,true);
				//3.设置回调
				xhr.onreadystatechange = function(){
					if(xhr.readyState == 4 && xhr.status == 200){
						//获取array字符串
						var arr = xhr.responseText;
						//字符串转换json对象
						var arr = JSON.parse(arr).val;
						console.log(arr)
							if(arr == '没有变化'){
								console.log('没有变化')
							}else if(arr[arr.length-1]=='over'){
								arr.pop();
								plusmapover(arr);
								console.log('游戏结束')
								$(function (){
									setTimeout("over()",100); //延迟1秒
								})
							}else{
								console.log(typeof arr)
								Setcookie('arr',arr);
								plusmap(arr);
								console.log('右键');
							}
					}
				}
				//4.发送请求
				xhr.send(null);
			};

			function plusmap(arr){
				document.getElementById('x1').innerText = arr[0][0];
				document.getElementById('x2').innerText = arr[0][1];
				document.getElementById('x3').innerText = arr[0][2];
				document.getElementById('x4').innerText = arr[0][3];
				document.getElementById('x5').innerText = arr[1][0];
				document.getElementById('x6').innerText = arr[1][1];
				document.getElementById('x7').innerText = arr[1][2];
				document.getElementById('x8').innerText = arr[1][3];
				document.getElementById('x9').innerText = arr[2][0];
				document.getElementById('x10').innerText = arr[2][1];
				document.getElementById('x11').innerText = arr[2][2];
				document.getElementById('x12').innerText = arr[2][3];
				document.getElementById('x13').innerText = arr[3][0];
				document.getElementById('x14').innerText = arr[3][1];
				document.getElementById('x15').innerText = arr[3][2];
				document.getElementById('x16').innerText = arr[3][3];
				document.getElementById('pp').innerText = arr[4]+'分';
				bianse()

			};

			function plusmapover(arr){
				document.getElementById('x1').innerText = arr[0][0];
				document.getElementById('x2').innerText = arr[0][1];
				document.getElementById('x3').innerText = arr[0][2];
				document.getElementById('x4').innerText = arr[0][3];
				document.getElementById('x5').innerText = arr[1][0];
				document.getElementById('x6').innerText = arr[1][1];
				document.getElementById('x7').innerText = arr[1][2];
				document.getElementById('x8').innerText = arr[1][3];
				document.getElementById('x9').innerText = arr[2][0];
				document.getElementById('x10').innerText = arr[2][1];
				document.getElementById('x11').innerText = arr[2][2];
				document.getElementById('x12').innerText = arr[2][3];
				document.getElementById('x13').innerText = arr[3][0];
				document.getElementById('x14').innerText = arr[3][1];
				document.getElementById('x15').innerText = arr[3][2];
				document.getElementById('x16').innerText = arr[3][3];
				bianse()
			};

			function over(){
				var num = document.getElementById('pp').innerText;
				var name = prompt("您的分数为:"+num+',恭喜您!进入了排行榜,请留下您的大名:');
				if(name){
					 //输出word的格式
					 topten(num,name);
				}else{
					topten(num,'无名');
				}

			};

			function topten(num,name){
				//1.创建xhr
				var xhr = createXhr();
				//2.创建请求
				var url = '/ht2048/toptenadd/?num='+num+'&name='+name;
				xhr.open('get',url,true);
				//3.设置回调
				xhr.onreadystatechange = function(){
					if(xhr.readyState == 4 && xhr.status == 200){
						console.log('记录排名')
					}
				}
				//4.发送请求
				xhr.send(null);
			};

			function bianse(){
				var x1 = document.getElementById("x1");
				if(x1.innerText == 0){
					x1.style.color = '#ede0c8';
				}else{
					x1.style.color = '#776e65';
				};
				var x2 = document.getElementById("x2");
				if(x2.innerText == 0){
					x2.style.color = '#ede0c8';
				}else{
					x2.style.color = '#776e65';
				};
				var x3 = document.getElementById("x3");
				if(x3.innerText == 0){
					x3.style.color = '#ede0c8';
				}else{
					x3.style.color = '#776e65';
				};
				var x4 = document.getElementById("x4");
				if(x4.innerText == 0){
					x4.style.color = '#ede0c8';
				}else{
					x4.style.color = '#776e65';
				};
				var x5 = document.getElementById("x5");
				if(x5.innerText == 0){
					x5.style.color = '#ede0c8';
				}else{
					x5.style.color = '#776e65';
				};
				var x6 = document.getElementById("x6");
				if(x6.innerText == 0){
					x6.style.color = '#ede0c8';
				}else{
					x6.style.color = '#776e65';
				};
				var x7 = document.getElementById("x7");
				if(x7.innerText == 0){
					x7.style.color = '#ede0c8';
				}else{
					x7.style.color = '#776e65';
				};
				var x8 = document.getElementById("x8");
				if(x8.innerText == 0){
					x8.style.color = '#ede0c8';
				}else{
					x8.style.color = '#776e65';
				};
				var x9 = document.getElementById("x9");
				if(x9.innerText == 0){
					x9.style.color = '#ede0c8';
				}else{
					x9.style.color = '#776e65';
				};
				var x10 = document.getElementById("x10");
				if(x10.innerText == 0){
					x10.style.color = '#ede0c8';
				}else{
					x10.style.color = '#776e65';
				};
				var x11 = document.getElementById("x11");
				if(x11.innerText == 0){
					x11.style.color = '#ede0c8';
				}else{
					x11.style.color = '#776e65';
				};
				var x12 = document.getElementById("x12");
				if(x12.innerText == 0){
					x12.style.color = '#ede0c8';
				}else{
					x12.style.color = '#776e65';
				};
				var x13 = document.getElementById("x13");
				if(x13.innerText == 0){
					x13.style.color = '#ede0c8';
				}else{
					x13.style.color = '#776e65';
				};
				var x14 = document.getElementById("x14");
				if(x14.innerText == 0){
					x14.style.color = '#ede0c8';
				}else{
					x14.style.color = '#776e65';
				};
				var x15 = document.getElementById("x15");
				if(x15.innerText == 0){
					x15.style.color = '#ede0c8';
				}else{
					x15.style.color = '#776e65';
				};
				var x16 = document.getElementById("x16");
				if(x16.innerText == 0){
					x16.style.color = '#ede0c8';
				}else{
					x16.style.color = '#776e65';
				};
			}