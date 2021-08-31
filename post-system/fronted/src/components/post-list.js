import PostItem from "./post-item";
import {memo} from 'react'

const PostList = (props) => {
    const { data } = props;

    return (
        <div>
            {data.map(item => {
                return <PostItem key={item.id} title={item.title} description={item.description} />
            })}
        </div>
    )
}

export default memo(PostList);