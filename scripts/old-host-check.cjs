const { chromium } = require('@playwright/test');
(async()=>{
 const browser=await chromium.launch({channel:'msedge',headless:true});
 try{
  const page=await browser.newPage();
  const response=await page.goto('https://rapimotion.ismailstudio.my/');
  const chain=[];for(let r=response.request();r;r=r.redirectedFrom())chain.unshift(r.url());
  const data={time:new Date().toISOString(),status:response.status(),final_url:page.url(),request_chain:chain,headers:await response.allHeaders(),title:await page.title(),robots:await page.locator('meta[name=robots]').getAttribute('content')};
  console.log(JSON.stringify(data));
 } finally {await browser.close();}
})().catch(e=>{console.error(e);process.exit(1)});
