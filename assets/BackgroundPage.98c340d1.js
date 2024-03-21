import{c as re,b as X,a as ae,h as se,e as ue}from"./render.bedc93c9.js";import{c as V,n as ce,d as de,e as j,p as W,i as Z,s as K,j as Y,r as R,q as f,w as $,b as J,u as me,x as p,V as ve,a7 as fe,a8 as pe,t as oe,o as le,H as ee,a9 as he,L as ge,M as _e,N as w,P as a,O as P,T as be,aa as ye,Q as x}from"./index.97c51684.js";import{g as te,s as ne,c as we}from"./selection.0c71da57.js";import{d as Pe,b as xe}from"./Ripple.380edac8.js";import{Q as H}from"./QBtn.f07215a0.js";import{u as Ce,a as qe}from"./use-dark.bd71bfe5.js";import{Q as ke,b as O,a as U}from"./QPage.94562b67.js";import{Q as Se}from"./QImg.062b8a64.js";import"./use-size.8c1e5cd2.js";import"./QSpinner.e9b89df9.js";function Ie(e){const n=[.06,6,50];return typeof e=="string"&&e.length&&e.split(":").forEach((r,s)=>{const l=parseFloat(r);l&&(n[s]=l)}),n}var Fe=re({name:"touch-swipe",beforeMount(e,{value:n,arg:r,modifiers:s}){if(s.mouse!==!0&&V.has.touch!==!0)return;const l=s.mouseCapture===!0?"Capture":"",t={handler:n,sensitivity:Ie(r),direction:te(s),noop:ce,mouseStart(o){ne(o,t)&&de(o)&&(j(t,"temp",[[document,"mousemove","move",`notPassive${l}`],[document,"mouseup","end","notPassiveCapture"]]),t.start(o,!0))},touchStart(o){if(ne(o,t)){const u=o.target;j(t,"temp",[[u,"touchmove","move","notPassiveCapture"],[u,"touchcancel","end","notPassiveCapture"],[u,"touchend","end","notPassiveCapture"]]),t.start(o)}},start(o,u){V.is.firefox===!0&&W(e,!0);const g=Z(o);t.event={x:g.left,y:g.top,time:Date.now(),mouse:u===!0,dir:!1}},move(o){if(t.event===void 0)return;if(t.event.dir!==!1){K(o);return}const u=Date.now()-t.event.time;if(u===0)return;const g=Z(o),_=g.left-t.event.x,c=Math.abs(_),h=g.top-t.event.y,m=Math.abs(h);if(t.event.mouse!==!0){if(c<t.sensitivity[1]&&m<t.sensitivity[1]){t.end(o);return}}else if(window.getSelection().toString()!==""){t.end(o);return}else if(c<t.sensitivity[2]&&m<t.sensitivity[2])return;const b=c/u,C=m/u;t.direction.vertical===!0&&c<m&&c<100&&C>t.sensitivity[0]&&(t.event.dir=h<0?"up":"down"),t.direction.horizontal===!0&&c>m&&m<100&&b>t.sensitivity[0]&&(t.event.dir=_<0?"left":"right"),t.direction.up===!0&&c<m&&h<0&&c<100&&C>t.sensitivity[0]&&(t.event.dir="up"),t.direction.down===!0&&c<m&&h>0&&c<100&&C>t.sensitivity[0]&&(t.event.dir="down"),t.direction.left===!0&&c>m&&_<0&&m<100&&b>t.sensitivity[0]&&(t.event.dir="left"),t.direction.right===!0&&c>m&&_>0&&m<100&&b>t.sensitivity[0]&&(t.event.dir="right"),t.event.dir!==!1?(K(o),t.event.mouse===!0&&(document.body.classList.add("no-pointer-events--children"),document.body.classList.add("non-selectable"),we(),t.styleCleanup=T=>{t.styleCleanup=void 0,document.body.classList.remove("non-selectable");const q=()=>{document.body.classList.remove("no-pointer-events--children")};T===!0?setTimeout(q,50):q()}),t.handler({evt:o,touch:t.event.mouse!==!0,mouse:t.event.mouse,direction:t.event.dir,duration:u,distance:{x:c,y:m}})):t.end(o)},end(o){t.event!==void 0&&(Y(t,"temp"),V.is.firefox===!0&&W(e,!1),t.styleCleanup!==void 0&&t.styleCleanup(!0),o!==void 0&&t.event.dir!==!1&&K(o),t.event=void 0)}};if(e.__qtouchswipe=t,s.mouse===!0){const o=s.mouseCapture===!0||s.mousecapture===!0?"Capture":"";j(t,"main",[[e,"mousedown","mouseStart",`passive${o}`]])}V.has.touch===!0&&j(t,"main",[[e,"touchstart","touchStart",`passive${s.capture===!0?"Capture":""}`],[e,"touchmove","noop","notPassiveCapture"]])},updated(e,n){const r=e.__qtouchswipe;r!==void 0&&(n.oldValue!==n.value&&(typeof n.value!="function"&&r.end(),r.handler=n.value),r.direction=te(n.modifiers))},beforeUnmount(e){const n=e.__qtouchswipe;n!==void 0&&(Y(n,"main"),Y(n,"temp"),V.is.firefox===!0&&W(e,!1),n.styleCleanup!==void 0&&n.styleCleanup(),delete e.__qtouchswipe)}});function Te(){const e=new Map;return{getCache:function(n,r){return e[n]===void 0?e[n]=r:e[n]},getCacheWithFn:function(n,r){return e[n]===void 0?e[n]=r():e[n]}}}const Ee={name:{required:!0},disable:Boolean},ie={setup(e,{slots:n}){return()=>p("div",{class:"q-panel scroll",role:"tabpanel"},X(n.default))}},$e={modelValue:{required:!0},animated:Boolean,infinite:Boolean,swipeable:Boolean,vertical:Boolean,transitionPrev:String,transitionNext:String,transitionDuration:{type:[String,Number],default:300},keepAlive:Boolean,keepAliveInclude:[String,Array,RegExp],keepAliveExclude:[String,Array,RegExp],keepAliveMax:Number},Ae=["update:modelValue","beforeTransition","transition"];function Be(){const{props:e,emit:n,proxy:r}=J(),{getCacheWithFn:s}=Te();let l,t;const o=R(null),u=R(null);function g(i){const d=e.vertical===!0?"up":"left";k((r.$q.lang.rtl===!0?-1:1)*(i.direction===d?1:-1))}const _=f(()=>[[Fe,g,void 0,{horizontal:e.vertical!==!0,vertical:e.vertical,mouse:!0}]]),c=f(()=>e.transitionPrev||`slide-${e.vertical===!0?"down":"right"}`),h=f(()=>e.transitionNext||`slide-${e.vertical===!0?"up":"left"}`),m=f(()=>`--q-transition-duration: ${e.transitionDuration}ms`),b=f(()=>typeof e.modelValue=="string"||typeof e.modelValue=="number"?e.modelValue:String(e.modelValue)),C=f(()=>({include:e.keepAliveInclude,exclude:e.keepAliveExclude,max:e.keepAliveMax})),T=f(()=>e.keepAliveInclude!==void 0||e.keepAliveExclude!==void 0);$(()=>e.modelValue,(i,d)=>{const y=S(i)===!0?B(i):-1;t!==!0&&E(y===-1?0:y<B(d)?-1:1),o.value!==y&&(o.value=y,n("beforeTransition",i,d),me(()=>{n("transition",i,d)}))});function q(){k(1)}function M(){k(-1)}function A(i){n("update:modelValue",i)}function S(i){return i!=null&&i!==""}function B(i){return l.findIndex(d=>d.props.name===i&&d.props.disable!==""&&d.props.disable!==!0)}function z(){return l.filter(i=>i.props.disable!==""&&i.props.disable!==!0)}function E(i){const d=i!==0&&e.animated===!0&&o.value!==-1?"q-transition--"+(i===-1?c.value:h.value):null;u.value!==d&&(u.value=d)}function k(i,d=o.value){let y=d+i;for(;y>-1&&y<l.length;){const F=l[y];if(F!==void 0&&F.props.disable!==""&&F.props.disable!==!0){E(i),t=!0,n("update:modelValue",F.props.name),setTimeout(()=>{t=!1});return}y+=i}e.infinite===!0&&l.length!==0&&d!==-1&&d!==l.length&&k(i,i===-1?l.length:-1)}function L(){const i=B(e.modelValue);return o.value!==i&&(o.value=i),!0}function Q(){const i=S(e.modelValue)===!0&&L()&&l[o.value];return e.keepAlive===!0?[p(fe,C.value,[p(T.value===!0?s(b.value,()=>({...ie,name:b.value})):ie,{key:b.value,style:m.value},()=>i)])]:[p("div",{class:"q-panel scroll",style:m.value,key:b.value,role:"tabpanel"},[i])]}function v(){if(l.length!==0)return e.animated===!0?[p(ve,{name:u.value},Q)]:Q()}function I(i){return l=Pe(X(i.default,[])).filter(d=>d.props!==null&&d.props.slot===void 0&&S(d.props.name)===!0),l.length}function N(){return l}return Object.assign(r,{next:q,previous:M,goTo:A}),{panelIndex:o,panelDirectives:_,updatePanelsList:I,updatePanelIndex:L,getPanelContent:v,getEnabledPanels:z,getPanels:N,isValidPanelName:S,keepAliveProps:C,needsUniqueKeepAliveWrapper:T,goToPanelByOffset:k,goToPanel:A,nextPanel:q,previousPanel:M}}var G=ae({name:"QCarouselSlide",props:{...Ee,imgSrc:String},setup(e,{slots:n}){const r=f(()=>e.imgSrc?{backgroundImage:`url("${e.imgSrc}")`}:{});return()=>p("div",{class:"q-carousel__slide",style:r.value},X(n.default))}});let D=0;const Le={fullscreen:Boolean,noRouteFullscreenExit:Boolean},Ne=["update:fullscreen","fullscreen"];function Ve(){const e=J(),{props:n,emit:r,proxy:s}=e;let l,t,o;const u=R(!1);xe(e)===!0&&$(()=>s.$route.fullPath,()=>{n.noRouteFullscreenExit!==!0&&c()}),$(()=>n.fullscreen,h=>{u.value!==h&&g()}),$(u,h=>{r("update:fullscreen",h),r("fullscreen",h)});function g(){u.value===!0?c():_()}function _(){u.value!==!0&&(u.value=!0,o=s.$el.parentNode,o.replaceChild(t,s.$el),document.body.appendChild(s.$el),D++,D===1&&document.body.classList.add("q-body--fullscreen-mixin"),l={handler:c},ee.add(l))}function c(){u.value===!0&&(l!==void 0&&(ee.remove(l),l=void 0),o.replaceChild(s.$el,t),u.value=!1,D=Math.max(0,D-1),D===0&&(document.body.classList.remove("q-body--fullscreen-mixin"),s.$el.scrollIntoView!==void 0&&setTimeout(()=>{s.$el.scrollIntoView()})))}return pe(()=>{t=document.createElement("span")}),oe(()=>{n.fullscreen===!0&&_()}),le(c),Object.assign(s,{toggleFullscreen:g,setFullscreen:_,exitFullscreen:c}),{inFullscreen:u,toggleFullscreen:g}}const De=["top","right","bottom","left"],Me=["regular","flat","outline","push","unelevated"];var ze=ae({name:"QCarousel",props:{...Ce,...$e,...Le,transitionPrev:{type:String,default:"fade"},transitionNext:{type:String,default:"fade"},height:String,padding:Boolean,controlColor:String,controlTextColor:String,controlType:{type:String,validator:e=>Me.includes(e),default:"flat"},autoplay:[Number,Boolean],arrows:Boolean,prevIcon:String,nextIcon:String,navigation:Boolean,navigationPosition:{type:String,validator:e=>De.includes(e)},navigationIcon:String,navigationActiveIcon:String,thumbnails:Boolean},emits:[...Ne,...Ae],setup(e,{slots:n}){const{proxy:{$q:r}}=J(),s=qe(e,r);let l=null,t;const{updatePanelsList:o,getPanelContent:u,panelDirectives:g,goToPanel:_,previousPanel:c,nextPanel:h,getEnabledPanels:m,panelIndex:b}=Be(),{inFullscreen:C}=Ve(),T=f(()=>C.value!==!0&&e.height!==void 0?{height:e.height}:{}),q=f(()=>e.vertical===!0?"vertical":"horizontal"),M=f(()=>`q-carousel q-panel-parent q-carousel--with${e.padding===!0?"":"out"}-padding`+(C.value===!0?" fullscreen":"")+(s.value===!0?" q-carousel--dark q-dark":"")+(e.arrows===!0?` q-carousel--arrows-${q.value}`:"")+(e.navigation===!0?` q-carousel--navigation-${z.value}`:"")),A=f(()=>{const v=[e.prevIcon||r.iconSet.carousel[e.vertical===!0?"up":"left"],e.nextIcon||r.iconSet.carousel[e.vertical===!0?"down":"right"]];return e.vertical===!1&&r.lang.rtl===!0?v.reverse():v}),S=f(()=>e.navigationIcon||r.iconSet.carousel.navigationIcon),B=f(()=>e.navigationActiveIcon||S.value),z=f(()=>e.navigationPosition||(e.vertical===!0?"right":"bottom")),E=f(()=>({color:e.controlColor,textColor:e.controlTextColor,round:!0,[e.controlType]:!0,dense:!0}));$(()=>e.modelValue,()=>{e.autoplay&&k()}),$(()=>e.autoplay,v=>{v?k():l!==null&&(clearTimeout(l),l=null)});function k(){const v=he(e.autoplay)===!0?Math.abs(e.autoplay):5e3;l!==null&&clearTimeout(l),l=setTimeout(()=>{l=null,v>=0?h():c()},v)}oe(()=>{e.autoplay&&k()}),le(()=>{l!==null&&clearTimeout(l)});function L(v,I){return p("div",{class:`q-carousel__control q-carousel__navigation no-wrap absolute flex q-carousel__navigation--${v} q-carousel__navigation--${z.value}`+(e.controlColor!==void 0?` text-${e.controlColor}`:"")},[p("div",{class:"q-carousel__navigation-inner flex flex-center no-wrap"},m().map(I))])}function Q(){const v=[];if(e.navigation===!0){const I=n["navigation-icon"]!==void 0?n["navigation-icon"]:i=>p(H,{key:"nav"+i.name,class:`q-carousel__navigation-icon q-carousel__navigation-icon--${i.active===!0?"":"in"}active`,...i.btnProps,onClick:i.onClick}),N=t-1;v.push(L("buttons",(i,d)=>{const y=i.props.name,F=b.value===d;return I({index:d,maxIndex:N,name:y,active:F,btnProps:{icon:F===!0?B.value:S.value,size:"sm",...E.value},onClick:()=>{_(y)}})}))}else if(e.thumbnails===!0){const I=e.controlColor!==void 0?` text-${e.controlColor}`:"";v.push(L("thumbnails",N=>{const i=N.props;return p("img",{key:"tmb#"+i.name,class:`q-carousel__thumbnail q-carousel__thumbnail--${i.name===e.modelValue?"":"in"}active`+I,src:i.imgSrc||i["img-src"],onClick:()=>{_(i.name)}})}))}return e.arrows===!0&&b.value>=0&&((e.infinite===!0||b.value>0)&&v.push(p("div",{key:"prev",class:`q-carousel__control q-carousel__arrow q-carousel__prev-arrow q-carousel__prev-arrow--${q.value} absolute flex flex-center`},[p(H,{icon:A.value[0],...E.value,onClick:c})])),(e.infinite===!0||b.value<t-1)&&v.push(p("div",{key:"next",class:`q-carousel__control q-carousel__arrow q-carousel__next-arrow q-carousel__next-arrow--${q.value} absolute flex flex-center`},[p(H,{icon:A.value[1],...E.value,onClick:h})]))),ue(n.control,v)}return()=>(t=o(n),p("div",{class:M.value,style:T.value},[se("div",{class:"q-carousel__slides-container"},u(),"sl-cont",e.swipeable,()=>g.value)].concat(Q())))}}),Qe="/assets/1996-conference-bali_processed.57ff0990.jpg",je="/assets/1996-conference-participants_scaled.ec8c4e78.jpg",Oe="/assets/Dr-Ichimori-receiving-prize_2000x900.4d3f8ebe.jpg",Re="/assets/PacELF-books_white-bkgnd.b84415b2.jpg";const We={class:"q-pa-md q-gutter-md rows"},Ke=a("div",{class:"q-mt-md text-center absolute-top slide-text"},[a("div",{class:"text-h5"},"International Conference on the Control of Lymphatic Filariasis - Bali 1996")],-1),Ye=a("div",{class:"q-mt-md text-center absolute-bottom slide-text"},[a("div",{class:"text-h5"},"International Conference Participants - Bali 1996")],-1),He=a("div",{class:"q-mt-md text-center absolute-bottom slide-text"},[a("div",{class:"text-h5"},"Dr Ichimori receiving Yomiuri Intl Cooperation Prize")],-1),Ue=a("h5",null,"Pacific Programme for the Elimination of Lymphatic Filariasis",-1),Ge=a("p",null,[x("PacELF worked within the framework of the "),a("a",{href:"https://www.who.int/health-topics/lymphatic-filariasis#tab=tab_1",target:"_blank"}," Global Programme to Eliminate Filariasis"),x(", the "),a("a",{href:"https://www.who.int/westernpacific",target:"_blank"}," WHO Regional Office for the Western Pacific"),x(" and the "),a("a",{href:"https://www.who.int/westernpacific/about/how-we-work/pacific-support",target:"_blank"}," Division of Pacific Technical Support"),x(". ")],-1),Xe=a("p",null,[x(" PacELF, the first regional filariasis elimination programme, formed in 1999 as a network to coordinate the efforts in the twenty-two island countries and territories that are working to eliminate filariasis in the Pacific. The elimination strategy has two pillars: "),a("ol",null,[a("li",null," Annual mass drug administration (MDA) using diethylcarbamazine citrate (DEC), albendazole and/or ivermectin to stop transmission, and "),a("li",null," Clinical management of infections and support to minimize progression of morbidity and disability in those individuals that are already infected. ")])],-1),Je=a("p",null," PacELF countries classified as non endemic in 2000 were Guam, Nauru, Northern Mariana Islands, Pitcairn Island, Solomon Islands, and Tokelau. Of the remaining PacELF 16 endemic countries and territories, some have since achieved filariasis elimination, and others are moving closer to that goal. ",-1),Ze=a("ul",null,[a("li",null,"Vanuatu,"),a("li",null,"Republic of the Marshall Islands,"),a("li",null,"Niue,"),a("li",null,"Cook Islands,"),a("li",null,"Tonga,"),a("li",null,"Palau,"),a("li",null,"Wallis & Futuna"),a("li",null,"Kiribati.")],-1),et=a("ul",null,[a("li",null,"American Samoa,"),a("li",null,"Federated States of Micronesia,"),a("li",null,"Fiji,"),a("li",null,"French Polynesia,"),a("li",null,"Papua New Guinea,"),a("li",null,"Samoa,"),a("li",null,"Tuvalu,"),a("li",null,"New Caledonia.")],-1),tt=a("p",null,"Some Pacific countries recently introduced triple drug therapy by adding ivermectin to mass drug administration to accelerate their progress towards elimination. ",-1),nt=a("h6",null,"PacELF Publications",-1),it=a("ul",null,[a("li",null,[a("a",{href:"https://www.biomedcentral.com/collections/Filariasis",target:"_blank"}," https://www.biomedcentral.com/collections/Filariasis")]),a("li",null,[a("a",{href:"https://tropmedhealth.biomedcentral.com/articles/10.1186/s41182-017-0075-4",target:"_blank"}," https://tropmedhealth.biomedcentral.com/articles/10.1186/s41182-017-0075-4")])],-1),at=a("div",{class:"q-ma-md col-12 col-sm"},[a("h6",null,"PacELF books"),a("p",null,[x(" We published a book in 2023: "),a("em",null,"\u201CThe PacELF collection: PacELF scientific papers and Dr Kazuyo Ichimori\u2019s contribution in commemoration of the Yomiuri International Cooperation Prize 2022\u201D"),x(" which contains an updated bibliography of lymphatic filariasis in the Pacific, 1999-2020. It is available as hardcopy on request. ")])],-1),pt={__name:"BackgroundPage",setup(e){let n=R(1);return(r,s)=>(ge(),_e(ke,null,{default:w(()=>[a("div",We,[P(O,null,{default:w(()=>[P(ze,{animated:"",modelValue:be(n),"onUpdate:modelValue":s[0]||(s[0]=l=>ye(n)?n.value=l:n=l),arrows:"",infinite:"",padding:"",height:"300px","object-fit":"contain"},{default:w(()=>[P(G,{name:1,"img-src":Qe,class:"column no-wrap flex-centre"},{default:w(()=>[Ke]),_:1}),P(G,{name:2,"img-src":je},{default:w(()=>[Ye]),_:1}),P(G,{name:3,"img-src":Oe},{default:w(()=>[He]),_:1})]),_:1},8,["modelValue"])]),_:1}),P(O,null,{default:w(()=>[P(U,null,{default:w(()=>[Ue,Ge,Xe,Je,x(" As of 2024, eight PacELF countries have achieved validation of elimination since the start of the programme: "),Ze,x(" The remaining countries are still conducting surveillance or mass drug administration: "),et,tt]),_:1})]),_:1}),P(O,null,{default:w(()=>[P(U,null,{default:w(()=>[nt,x(" Progress by country with links to a bibliography of published literature from 1970 to mid 2017 is summarized in the following articles: "),it]),_:1})]),_:1}),P(O,null,{default:w(()=>[P(U,{class:"q-mx-md row"},{default:w(()=>[P(Se,{src:Re,alt:"PacELF book covers",fit:"contain","max-width":"500px",class:"col-12 col-sm-4"}),at]),_:1})]),_:1})])]),_:1}))}};export{pt as default};
